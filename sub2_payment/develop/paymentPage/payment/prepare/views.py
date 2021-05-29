from django.shortcuts import render
from .models import UserDeliveryInfo
from .models import OrderedBookList
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.


class Order(View):
    def get(self, request):
        book_list = False
        book_lists = OrderedBookList.objects.all()
        for item in book_lists:
            if item.user_id == 'user1':
                book_list = True
                book_list = item.books
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
            'message': message,
        }
        return render(request, 'prepare/result.html', context)



