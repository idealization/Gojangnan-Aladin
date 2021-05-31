from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    PACKING_FOR_SHIPPING = 'P'
    ON_DELIVERY = 'D'
    DELIVERY_OVER = 'O'

    STATE_CHOICE = [
        (PACKING_FOR_SHIPPING, 'Packing for shipping'),
        (ON_DELIVERY, 'On delivery'),
        (DELIVERY_OVER, 'Delivery over')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pay_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=1, choices=STATE_CHOICE, default=PACKING_FOR_SHIPPING)

    class Meta:
        db_table = 'Payment'
        ordering = ['pay_date']

    def __str__(self):
        return self.order_id


class OrderDeliveryInfo(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'OrderDeliberyInfo'

class OrderedBookList(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'OrderedBookList'

    def __str__(self):
        return self.product