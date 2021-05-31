from django.shortcuts import render
from .models import UserDeliveryInfo
from .models import OrderedBookList
from .models import Book
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.


class Order(View):
    def get(self, request):
        ordered_book_lists = OrderedBookList.objects.all()
        book_lists = Book.objects.all()
        book_list = []
        for item in ordered_book_lists:
            if item.ordered_user_id == 'user1':
                book_list.append(item.ordered_book_id)
                for book in book_lists:
                    if book.book_id == item.ordered_book_id:
                        book_list.append(book)
        context = {
            'book_list': book_list,
        }
        return render(request, 'prepare/order.html', context)

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
        return render(request, 'prepare/result.html', context)


