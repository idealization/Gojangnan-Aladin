from django.db import models

# Create your models here.


class UserDeliveryInfo(models.Model):
    user_name = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=50)


class OrderedBookList(models.Model):
    user_id = models.CharField(max_length=20)
    books = models.ForeignKey("Book", related_name="book", on_delete=models.CASCADE, db_column="book")


class Book(models.Model):
    title = models.CharField(max_length=30)
