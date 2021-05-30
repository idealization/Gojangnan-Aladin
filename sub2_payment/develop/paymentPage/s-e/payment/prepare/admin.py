from django.contrib import admin

# Register your models here.

from .models import UserDeliveryInfo
from .models import OrderedBookList
from .models import Book

admin.site.register(UserDeliveryInfo)
admin.site.register(OrderedBookList)
admin.site.register(Book)


