
from . import views
from .views import cart
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('',views.cart  , name='cart'),
    # path('<slug:category_slug>/',views.store  , name='product_by_category'),
    # path('<slug:category_slug>/<slug:product_slug>/',views.product_details  , name='product_details'),

] 
