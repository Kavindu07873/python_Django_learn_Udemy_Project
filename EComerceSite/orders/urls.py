
from . import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    # path('',views.store  , name='store'),
    path('place_order/',views.place_order  , name='place_order'),
    
    # path('category/<slug:category_slug>/',views.store  , name='product_by_category'),
    # path('category/<slug:category_slug>/<slug:product_slug>/',views.product_details  , name='product_details'),
    # path('search/' , views.search , name='search')

] 
