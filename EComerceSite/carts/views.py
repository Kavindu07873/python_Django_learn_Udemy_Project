from django.shortcuts import render ,redirect
from store.models import Product
from .models import Cart ,CartItem

# Create your views here.

#cookies wala thiyena session id eka ganne mehema private method ekakin 
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart    


def add_cart(request, product_id):
    product = Product.objects.get(id = product_id) # get the product

    # cookies wala thiyena cart_id eka gaththa Cart eke id eka widiyata
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))#get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

# dan thiyenawa product eka saha cart eka (product , cart)
# dan me product eka api danna ona cart eka athulata
# eka karanna api cartItem eka gannawa
# cartItem eke thiyenawa product / cart kiyala dekak
# methanin gaththa product ,cart deka assign karanawa e cartItem eke dekata
# antimeta url ekath wenas karanna ona
    try:
        cart_item = CartItem.objects.get(product =  product ,cart = cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')





def cart(request):
    return render(request , 'cart/cart.html')