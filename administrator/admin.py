from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemImg)
admin.site.register(DeliveryLocations)
admin.site.register(Sizes)
admin.site.register(Review)
admin.site.register(CartToken)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Station)
admin.site.register(Description)
admin.site.register(SiteSettings)