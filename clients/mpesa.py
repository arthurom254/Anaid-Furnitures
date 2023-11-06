from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
def index(request):
    cl = MpesaClient()
    phone_number = '0111496799'
    amount = 1
    transaction_desc = 'Business Payment Description'
    occassion = 'Test business payment occassion'
    callback_url = 'https://api.darajambili.com/b2c/result'
    response = cl.business_payment(phone_number, amount, transaction_desc, callback_url, occassion)
    return HttpResponse(response)