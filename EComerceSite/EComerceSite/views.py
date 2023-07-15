from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def home(request):
 
    return render(request ,'home.html' ,context)





