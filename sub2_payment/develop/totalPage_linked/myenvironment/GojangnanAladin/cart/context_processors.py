from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}

    else :
        try:
            user = request.user

            if user.is_authenticated:
                cart = Cart.objects.filter(user = request.user)
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
                for cart_item in cart_items:
                    item_count += cart_item.quantity

            else:
                raise Cart.DoesNotExist()

        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count = item_count)