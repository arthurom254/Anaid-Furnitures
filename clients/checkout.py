from django.shortcuts import render, redirect
from django.contrib import messages
from administrator.models import CartToken, Cart, Country, City, Station, PaymentInProgress, DeliveryLocations
from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
import uuid
from .utils import return_cart, total_amount, product_names, shipping_cost, fetchCookie
# Dont Wory, This is not for you to care about (0_0)
def information_guther(request):
    if request.user.is_authenticated:
        dlocation, created=DeliveryLocations.objects.get_or_create(user=request.user)
        if request.method == 'POST':
            station=request.POST['station']
            fname=request.POST['fname']
            lname=request.POST['lname']
            phone=request.POST['phone']
            dlocation.station = Station(id=station)
            dlocation.towndelivery='True'
            dlocation.phone=phone
            dlocation.fname=fname
            dlocation.lname=lname
            dlocation.save()
            return redirect('/checkout/payment')
        else:
            country=Country.objects.all()
            city=City.objects.all()
            station=Station.objects.all()
            dlocation.towndelivery='False'
            dlocation.save()
            context={
                'country':country,
                'city':city,
                'station':station,
                'dlocation':dlocation,
            }
            return render(request, 'clients/checkout_info.html', context)
    else:
        next=request.META['PATH_INFO']
        return redirect(f'/login?next={next}')
    
def payment(request):
    if request.user.is_authenticated:
        try:
            token=fetchCookie(request) 
            ctoken=CartToken.objects.get(token=token)
        except:
            token=None
            ctoken=None

        for cart in return_cart(request):
            if cart.qty > cart.item.available:
                if cart.item.available == 0:
                    cart.delete() 
                    print("Done Blue --> test 7 ")
                else:
                    cart.qty=cart.item.available
                    cart.price=cart.qty * cart.item.price
                    cart.save()
                messages.info(request, "Some of the Items Seems to have been Taken, we've updated your cart with the available ones")
            
        if Cart.objects.filter(token = ctoken).exists():
            host=request.get_host()
            invoice=str(uuid.uuid4())
            #remove this
            PaymentInProgress.objects.filter(user=request.user, payment_status='False').delete()
            #end Remove
            shipping=shipping_cost(request)
            total_amt=total_amount(request)
            total_amt += shipping
            # Pesapal start
            
            # End Pesapal
            paypal_dict = {
                "business": settings.PAYPAL_RECEIVER_EMAIL,
                "amount": total_amt,
                "currency_code": "USD",
                "item_name": product_names(request),
                'invoice':invoice,
                "notify_url": f'http://{host}{reverse("paypal-ipn")}',
                "return": f'http://{host}/payment-complete',
                "cancel_return": f'http://{host}/payment-failed',
                "custom": "plan",
            }
            paypal_payment_form=PayPalPaymentsForm(initial=paypal_dict)
            paid=PaymentInProgress.objects.create(user=request.user,invoice=invoice, gross_pay=total_amt, token=ctoken)
            paid.save()
            context={
                'shipping':shipping,
                'form':paypal_payment_form,
                'c_total_price':total_amt,
            }      
            return render(request, 'clients/checkout_pay.html', context)
        else:
            return redirect('/cart')
    else:
        next=request.META['PATH_INFO']
        return redirect(f'/login?next={next}')
    