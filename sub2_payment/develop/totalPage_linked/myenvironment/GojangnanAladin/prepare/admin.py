from django.contrib import admin

# Register your models here.

from .models import Order
from .models import OrderDeliveryInfo
from .models import OrderedBookList

admin.site.register(Order)
admin.site.register(OrderDeliveryInfo)
admin.site.register(OrderedBookList)


