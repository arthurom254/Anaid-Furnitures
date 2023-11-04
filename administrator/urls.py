from django.urls import path
from . import views
urlpatterns=[
    path('login', views.login, name='Log in'),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="Log out"),
    path('dashboard', views.dashboard, name='Admin Dashboard'),
    path('my', views.profile, name='User Profile'),
    path('orders', views.orders, name='Castomer Orders'),
    path('new', views.new, name='Create new Item'),
    path('edit', views.edit, name='Edit existing Product'),
    path('bloger', views.blog, name="New Blog")
    
]