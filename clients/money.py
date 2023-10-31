# from django_pesapal.views import PaymentRequestMixin, TemplateView

# class PaymentView(PaymentRequestMixin, TemplateView):

#     def get_pesapal_payment_iframe(self):

#         '''
#         Authenticates with pesapal to get the payment iframe src
#         '''
#         order_info = {
#             'first_name': 'Some',
#             'last_name': 'User',
#             'amount': 1,
#             'description': 'Payment for X',
#             'reference': 2,  # some object id
#             'email': 'user@example.com',
#         }

#         iframe_src_url = self.get_payment_url(**order_info)
#         return iframe_src_url