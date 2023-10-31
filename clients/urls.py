from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views, cart, checkout, search, api, tests, pesapal, money
# from mpesa.urls import mpesa_urls
# from .paypal_test import paypal_payment_received
# import django_pesapal
app_name='clients'
urlpatterns=[
    path('', views.home, name="Home"),
    # path('mpesa/', include(mpesa_urls)),
    # path('view/<str:id>', views.product_more_1, name="Product More Details" ),
    # path('checkout', views.checkout101, name='Checkout'),
    path('payment-complete', views.paypal_payment_complete, name="Checkout Payment Complete"),
    path('payment-failed', views.paypal_payment_failed, name="Checkout Payment Failed"),
    path('category/<str:category>', views.category_listing, name="Category Listing"),
    path('category/<str:category>/<str:id>', views.product_more, name="Product More Details"), 
    path('cart/', cart.view_cart, name="View Cart"),
    path('cart/<str:id>',cart.carts_fetch_set, name="carts_fetch_set" ),   
    path('checkout/information/',checkout.information_guther, name="Checkout Information"),
    path('checkout/payment/',checkout.payment, name="Checkout Information"),
    path('search', search.search_item, name="Search Request"),
    path('get/city/<str:id>', api.get_city, name="City"),
    path('get/station/<str:id>', api.get_station, name="Station"),
    # path(r'^payments/', include('django_pesapal.urls')),
    # path('money', money.PaymentView.get_pesapal_payment_iframe, name="money"),
    # path('pesapal/', pesapal.initiate_payment, name="Pay with pesapal"),
    # path('pesapal_ipn', pesapal.payment_ipn, name="Ipn pesapal"),
    # path('pesapal/done', pesapal.pesapal_callback, name="Pesapal Callback"),
    # path('test',tests.atom, name="Mail test"), 
    # path('py',money.PaymentView.get_pesapal_payment_iframe )   ,
]