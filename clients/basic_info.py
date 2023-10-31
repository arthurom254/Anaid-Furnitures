from administrator.models import Cart, CartToken, Category, SiteSettings
from django.db.models import Sum

def information(request):
    categry=Category.objects.all()[:16]
    info=SiteSettings.objects.filter().first()

    try:
        site_name=info.sites_name
    except:
        site_name='Atom'

    try:
        token=request.COOKIES.get('cart_cookie')
        cart_token=CartToken.objects.get(token=token)
        cart=Cart.objects.filter(token=cart_token)
        try:
            cart_count=cart.aggregate(Sum('qty'))
            cart_count=cart_count['qty__sum']
        except:
            cart_count=0

        total_price=cart.aggregate(Sum('price'))
        total_price=total_price['price__sum']
        total_tax=int(total_price)*0.16
        total_tax=round(total_tax,2)
    except:
        cart=None
        cart_count=0
        total_price=0
        total_tax=0
    context={
        'site_name':site_name,
        'cart':cart,
        'category':categry,
        'cart_count':cart_count,
        'total_price':total_price,
        'total_tax':round(total_tax, 2),
        'info':info,
    }
    return context


