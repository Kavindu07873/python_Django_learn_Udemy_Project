from django.shortcuts import get_object_or_404, render ,redirect
from store.models import Product,Variation
from .models import Cart ,CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
# Create your views here.

#cookies wala thiyena session id eka ganne mehema private method ekakin 
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart    


def add_cart(request, product_id):
    product = Product.objects.get(id = product_id) # get the product
    product_variation= [] 
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]

            try :
                variation = Variation.objects.get(variation_category__iexact = key ,variation_value__iexact=value)
                product_variation.append(variation)
                # print(variation)
                 
            except:
                pass
        # return HttpResponse(color + ' '+ size)
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
    
    
    # mulinma api cartitem eken ena ekai api gawa thiyena product ekai cart ekai samanada balanawa
    #  etapasse exists() kiyana eken gannawa eka True or False da kiyala
    # assing karanawa is_cart_item_exists
    is_cart_item_exists = CartItem.objects.filter(product= product , cart = cart).exists()
    
    # if ekak aragena True nm
    if is_cart_item_exists:
        cart_item = CartItem.objects.filter(product =product ,cart = cart)
        
        #existing_variation --> database
        # current variation --> product_variation
        # item_id -> database  
        
        ex_var_list = []
        id = []

        for item in cart_item:
            existing_variation = item.variations.all()
            # api list ekak widiyata ganna ona
            ex_var_list.append(list(existing_variation))
            id.append(item.id)

        print(ex_var_list)
        # if ekak dala
        if product_variation in ex_var_list:
            # return HttpResponse('true')
            index = ex_var_list.index(product_variation)
            item_id = id[index]
            item = CartItem.objects.get(product = product , id = item_id)
            item.quantity += 1
            print("kalina add nm meka wada karanne")
            item.save()
        else:
            item = CartItem.objects.create(product = product,quantity =1 , cart =cart)
            # return HttpResponse('false')
            # methana product variation eka empty da kiyala balanawa me if eken
            if len(product_variation) >0:
                item.variations.clear()
                item.variations.add(*product_variation)
                print("aluthen add nm meka wada")
                item.save()
    else :
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        if len(product_variation) >0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)
            print("danne na ai kiyala")
            cart_item.save()
    return redirect('cart')


def remove_cart(request , product_id ,cart_item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product , id = product_id)
    try:
        cart_item = CartItem.objects.get(product = product , cart = cart ,id = cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')


def remove_cart_item(request , product_id ,cart_item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product , id = product_id)
    cart_item = CartItem.objects.get(product = product , cart = cart , id = cart_item_id)
    cart_item.delete()
    return redirect('cart')





def cart(request ,total =0 ,quantity=0 ,cart_items = None):
    try:
        tax =0
        grand_total = 0
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart , is_active =True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        
        tax = (2 * total)/100
        grand_total  = total +tax

    except ObjectDoesNotExist:
        pass

    context ={
            'total' : total,
            'quantity':quantity,
            'cart_items' : cart_items,
            'tax':tax,
            'grand_total' : grand_total
        }

    return render(request , 'cart/cart.html' ,context)
