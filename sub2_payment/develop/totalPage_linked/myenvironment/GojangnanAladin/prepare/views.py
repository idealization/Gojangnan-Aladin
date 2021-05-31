from django.shortcuts import render, redirect
from .models import Order
from .models import OrderDeliveryInfo
from .models import OrderedBookList
from .models import Product
from cart.models import Cart, CartItem
from cart.views import _cart_id
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.views.generic import View

# Create your views here.
class Ordering(View):

    # @login_required(login_url='account:login')
    def get(self, request):
        try:
            user = request.user

            if user.is_authenticated:
                total = 0
                counter = 0
                ordered_books = None

                cart = Cart.objects.get(user = request.user)
                ordered_books = CartItem.objects.filter(cart=cart, activate=True)
                for ordered_book in ordered_books:
                    total += (ordered_book.product.price * ordered_book.quantity)
                    counter += ordered_book.quantity
            else:
                raise ObjectDoesNotExist()

        except ObjectDoesNotExist:
            pass

        return render(request, 'prepare/order.html', dict(ordered_books = ordered_books, total = total, counter = counter))

    # @login_required(login_url='account:login')
    def post(self, request):
        name = request.POST.get('user_name')
        phone = request.POST.get('user_phone')
        address = request.POST.get('user_address')
        message = False
        if name and phone and address:
            message = True
        message = 'Your order has been placed, ' + name
        context = {
            'name': name,
            'phone': phone,
            'address': address,
            'message': message,
        }


        cart = Cart.objects.get(user = request.user)

        total = 0
        counter = 0
        ordered_books = None

        # cart = Cart.objects.get(user = request.user)
        ordered_books = CartItem.objects.filter(cart=cart, activate=True)
        for ordered_book in ordered_books:
            total += (ordered_book.product.price * ordered_book.quantity)
            counter += ordered_book.quantity

        order = Order.objects.create(
            user = request.user,
            price = total
        )
        order.save()

        deliveryInfo = OrderDeliveryInfo.objects.create(
            order = order,
            user_name = name,
            user_phone = phone,
            user_address = address,
        )
        deliveryInfo.save()

        for ordered_book in ordered_books:
            orderedBook = OrderedBookList.objects.create(
                order = order,
                product = ordered_book.product,
                quantity = ordered_book.quantity,
            )
            orderedBook.save()

        for ordered_book in ordered_books:
            orderedBook = Product.objects.get(id=ordered_book.product.id)
            orderedBook.stock -= ordered_book.quantity
            orderedBook.save()

        ordered_books.delete()
        cart.delete()


        return render(request, 'prepare/result.html', context)