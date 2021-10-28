from restaurant_sys.models import dish, restaurant, bill_item, bill_order
from django.contrib import admin
from .views import *
# Register your models here.
admin.site.register(restaurant)
admin.site.register(dish)
admin.site.register(bill_item)
admin.site.register(bill_order)