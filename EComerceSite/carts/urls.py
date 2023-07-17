
from . import views
from .views import cart
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('',views.cart  , name='cart'),
    path('add_cart/<int:product_id>/',views.add_cart  , name='add_cart'),
    # path('<slug:category_slug>/<slug:product_slug>/',views.product_details  , name='product_details'),

] 
