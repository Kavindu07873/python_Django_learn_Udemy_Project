
from . import views
from .views import store
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('',views.store  , name='store'),
    path('<slug:category_slug>/',views.store  , name='product_by_category'),
] 
