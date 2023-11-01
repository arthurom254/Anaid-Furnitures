from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.http import HttpResponse
from administrator.models import UserProfile, Category, Item, Review, Order, Cart, CartToken
from django.contrib.auth.decorators import login_required
import uuid
from django.contrib import messages
from django.db.models import Sum, Q
# from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# Home Page View, the first page you see when you visit the website in url="https://example.com/"
def home(request):
    item=Item.objects.filter(outofstalk='False')[:16]
    print(request.path)
    context={
        'item':item,
    }
    return render(request, 'clients/index.html', context)

# This is the page you see when you click a specific category e.g url: https://example.com/category/<category_name>
def category_listing(request, category):    
    category_1=Category.objects.get(title=category)
    item=Item.objects.filter(category=category_1, outofstalk='False')[:12]
    context={
        'item':item
    }
    return render(request, 'clients/category_listing.html', context)
# This page gives more description about a product e.g https://example.com/category/<category-nae>/<item-id>
def product_more(request, category, id):
    product=get_object_or_404(Item,id=id)
    next=request.META['PATH_INFO']
    if request.method== 'POST':
        if request.user.is_authenticated:
            title=request.POST['title']
            star=request.POST['stars']
            if star>'0' and star<='5':
                stars=star
            else:
                stars=5
            body=request.POST['body']
            revi, created=Review.objects.get_or_create(user=request.user,item=product )
            revi.title=title
            revi.stars = stars
            revi.text=body
            revi.save()
            messages.success(request, 'Thank you for submitting you review')
            return redirect(next)
        else:
            
            return redirect(f'/login?next={next}')
    else:
        
        category_1=Category.objects.get(title=category)
        related=Item.objects.filter(category=category_1).exclude(id=id)[:12]
        review = Review.objects.filter(item=Item(id=id))
        total_review=review.count()
        try:
            token=request.COOKIES.get('cart_cookie')
            cart_token=CartToken.objects.get(token=token)
            cart=Cart.objects.get(token=cart_token,item=Item(id=id) )
            mycart=cart.qty
        except:
            mycart=''
        r1=Review.objects.filter(Q(stars__gte=1,stars__lt=2 ), item=product).count()
        r2=Review.objects.filter(Q(stars__gte=2,stars__lt=3 ), item=product).count()
        r3=Review.objects.filter(Q(stars__gte=3,stars__lt=4 ), item=product).count()
        r4=Review.objects.filter(Q(stars__gte=4,stars__lt=5 ), item=product).count()
        r5=Review.objects.filter(stars=5, item=product).count()
        
        try:
            review_each=[{'r':r1, 'count':1, 'p':r1/total_review*100}, {'r':r2, 'count':2, 'p':r2/total_review*100}, {'r':r3, 'count':3, 'p':r3/total_review*100}, {'r':r4, 'count':4, 'p':r4/total_review*100}, {'r':r5, 'count':5, 'p':r5/total_review*100}]
        except:
            review_each=None
        try:
            total_stars=review.aggregate(Sum('stars'))
            total_stars=round(total_stars['stars__sum']/total_review, 1)
            if not total_stars:
                total_stars=0
        except:
            total_stars=0
        
    
        context={
            'product':product,
            'related': related,
            'review':review[:10],
            'total_stars':total_stars,
            'review_each':review_each,
            'mycart':mycart
        }
        return render(request, 'clients/product_more.html', context)

#This was a test view, it is not usefull (0_0)
def product_more_1(request, id):
    product=Item.objects.get(id=id)
    context={
        'product':product,
    }
    return render(request, 'clients/product_more.html', context)

#@login_required
#This was a test view, it is not usefull (0_0)
def checkout101(request):
    host=request.get_host()
    paypal_dict={
        'business':settings.PAYPAL_RECEIVER_EMAIL,
        'amount':45,
        'item_name':'33',
        'invoice':uuid.uuid4(),
        'currency_code':'USD',
        'notify_url':f'http://{host}/{reverse("paypal-ipn")}',
        'return_url':f'http://{host}/payment-complete',
        'cancel_url':f'http://{host}/payment-failed',
    }
    paypal_payment_form=PayPalPaymentsForm(initial=paypal_dict)
    context={
        'form':paypal_payment_form,
    }
    return render(request, 'clients/checkout.html', context)

# THe Page you get redirected to after completing paypal payment
def paypal_payment_complete(request):
    if request.user.is_authenticated:
        order=Order.objects.filter(user=User(id=request.user.id))
        context={
            'order':order,
        }
        return render(request, 'clients/orders.html', context)
    else:
        try:
            next=request.META['PATH_INFO'] 
        except:
            next='/'

        return redirect(f'login?next={next}')

# THe Page you get redirected to after paypal payment fails

def paypal_payment_failed(request): 
    return render(request, 'clients/failed.html')


