from django.shortcuts import render ,get_object_or_404
from .models import Product
from .models import Category
from carts.models import CartItem
from carts.views import _cart_id

from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def store(request,category_slug=None):
    categories = None
    products =None

    if category_slug != None:
        categories = get_object_or_404(Category ,slug = category_slug)
        products   =Product.objects.all().filter(category = categories , is_available=True)
        paginator = Paginator(products , 3)
        page = request.GET.get('page')
        page_product = paginator.get_page(page)
        product_count = products.count()
    else:
        products =Product.objects.all().filter(is_available =True)
        paginator = Paginator(products , 3)
        page = request.GET.get('page')
        page_product = paginator.get_page(page)
        product_count = products.count()
    
    context = {

        'products':page_product,
        'product_count':product_count
    }
    return render(request , 'store/store.html' , context)

# def product_by_category(request ,category_slug ):
#     categories =None
#     products =None
#     categories = get_object_or_404(Category,slug = category_slug )
#     products = Product.objects.all().filter(Category =categories ,is_available = True)
#     product_count = products.count()
#     context = {
#         'products':products,
#         'product_count':product_count
#     }
#     return render(request , 'store/store.html' , context)


def product_details(request ,category_slug,product_slug ):
    try:
        # category__slug mehema __ dekak dala apita puluwan vena app ekaka thiyenma model ekaka atribute ekak access karanna
        single_product = Product.objects.get(category__slug = category_slug , slug = product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request) , product = single_product).exists()
    except Exception as e:
        raise e
    
    context = {
        'single_product':single_product,
        'in_cart' : in_cart,

    }

    return render(request , 'store/product_details.html' ,context)

