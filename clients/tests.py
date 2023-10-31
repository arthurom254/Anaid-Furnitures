from django.test import TestCase
from .utils import send_mail_after_order, return_cart
from django.http import HttpResponse

def atom(request):    
    try:
        send_mail_after_order(request.user, return_cart(request))
        return HttpResponse("sent")
    except:
        return HttpResponse("Not sent")



