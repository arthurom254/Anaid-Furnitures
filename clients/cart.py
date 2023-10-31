from administrator.models import Cart, CartToken, Item
from django.http import HttpResponse
from django.db.models import Sum
from django.shortcuts import render
from .utils import keygen, fetchCookie

def set_cart_to_bd(request, token, id):
        try:
            add=int(request.GET.get('add'))
        except:
            add=1            
        item=Item.objects.get(id=id)
        price=add*int(item.price)
        max=int(item.available)
        newtoken, created=CartToken.objects.get_or_create(token=token)
        if add > 0 and add <= max:
            if Cart.objects.filter(item=Item(id=id), token=newtoken):
                updater=Cart.objects.get(item=Item(id=id), token=newtoken)
                updater.qty=add
                updater.price=price
                updater.save()
            else:
                new=Cart.objects.create(item=Item(id=id), token=newtoken, qty=add, price=price)
                new.save()
        elif add == 0:
            Cart.objects.get(item=Item(id=id), token=newtoken).delete()
        else:
            pass
        count=Cart.objects.filter(token=newtoken)
        num=count.aggregate(Sum('qty'))
        return num['qty__sum']

def carts_fetch_set(request, id):
    if fetchCookie(request):
        token=fetchCookie(request)
        count=set_cart_to_bd(request, token, id)
        return HttpResponse(f"{count}")
        
    else:
        token=keygen()
        count=set_cart_to_bd(request, token, id)
        response=HttpResponse(count)
        response.set_cookie('cart_cookie', token)
        return response

def view_cart(request):
    return render(request, 'clients/cart.html')

