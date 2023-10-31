
from administrator.models import Order, PaymentInProgress, Cart, Item
from django.dispatch import receiver
from django.conf import settings
from .utils import send_mail_after_order
from threading import Thread
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
def do_update(sender):
    ipn_obj = sender
    if ipn_obj.payment_status == 'Completed':
        print("Test 2: valid-status-complete")
        invoice=ipn_obj.invoice
        payment_in_progress=PaymentInProgress.objects.get(invoice=invoice)
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL or  ipn_obj.mc_gross != payment_in_progress.gross_pay or ipn_obj.mc_currency != 'USD':
            # This Transaction Has Been Interfered With, If you think this is an error please contuct us # 
            print("Test 3: Payment Declined")
            return 0
        else:
            print("Test 4: Payment Success")
            cart=Cart.objects.filter(token=payment_in_progress.token)
            ##############################################################
            for items in cart:

                order=Order.objects.create(invoice=invoice, user=payment_in_progress.user, item=items.item, qty=items.qty,price=items.price,payment_status='True')
                
                order.save()
                
                items.item.available-=items.qty
                items.item.save()

                print("Test 5: DB Updated")
            ##############################################################

            def send_mail_now(x,y):
                send_mail_after_order(x,y)
            t1=Thread(target=send_mail_now, args=[payment_in_progress.user, cart])
            t1.start()

            cart.delete()

            return 1
    else:
        print("Test 6: Payment Incomplete or Cancelled")
        return ('Paypal payment status not completed: %s' % ipn_obj.payment_status)
    


@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    print("Test 1: valid-ipn")
    do_update(sender)



@receiver(invalid_ipn_received)
def invalid_paypal_payment_received(sender, **kwargs):
    print("Test 7: invalid-ipn")
    do_update(sender)