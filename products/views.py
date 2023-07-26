from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Offer


# Create your views here.
def index(request):
    dict_products={
        'products' : Product.objects.all()
    }
    return render(request,'index.html',dict_products)


def about(request):
    return HttpResponse("<h1>This is About Page</h1>")

def contact(request):
    return HttpResponse("<h1>This is Contact Page</h1>")

