from django.db import models

# Create your models here.


class UserDeliveryInfo(models.Model):
    user_name = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=50)


class OrderedBookList(models.Model):
    ordered_user_id = models.CharField(max_length=20)
    ordered_book_id = models.CharField(max_length=20)


class Book(models.Model):
    book_id = models.CharField(max_length=20)
    book_title = models.CharField(max_length=30)
    book_author = models.CharField(max_length=20)
