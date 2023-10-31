from administrator.models import DeliveryLocations, CartToken, Cart
from django.db.models import Sum
import uuid
from .mails import SendEmail

def host(request):
    return request.get_host()

def return_cart(request):
    token=request.COOKIES.get('cart_cookie')
    cart_token=CartToken.objects.get(token=token)
    cart=Cart.objects.filter(token=cart_token)    
    return cart

def keygen():
    return f'atom_{uuid.uuid4()}'

def fetchCookie(request):
    token=request.COOKIES.get('cart_cookie')
    return token


def total_amount(request):
    try:
        cart=return_cart(request)
        total_price=cart.aggregate(Sum('price'))
        total_price=int(total_price['price__sum'])
    except:
        total_price=0

    return total_price


def product_names(request):
    cart=return_cart(request)
    x=[]
    for name in cart:
        x.append(f'{name.qty}-{name.item.title},')
    y="".join(x)
    return f'{y}'

def shipping_cost(request):
    dlocation, created=DeliveryLocations.objects.get_or_create(user=request.user)
    if dlocation.towndelivery == 'True':
        return dlocation.station.prce
    else:
        return 0
    

def send_mail_after_order(user, cart):
    client=SendEmail(
                        to=user.email,
                        subject="Order received by kipekee",
                        template="order",
                        context={"fname":user.first_name, "lname":user.last_name,"cart":cart},
                    )
    client.send()

    merchant=SendEmail(
                            to='admn@kipekee.com',
                            subject=f"{user.first_name}: {user.email} Placed an order",
                            template="order_merchant",
                            context={"fname":user.first_name, "lname":user.last_name,"cart":cart, "email":user.email},
                        )
    merchant.send()
    