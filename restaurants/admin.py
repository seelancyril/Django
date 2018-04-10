from django.contrib import admin
from .models import RestaurantLocation, OrderLocation
# Register your models here.
admin.site.register(RestaurantLocation)
admin.site.register(OrderLocation)