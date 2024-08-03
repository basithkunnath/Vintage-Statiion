from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def Product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    list_product=Product.objects.all()
    product_paginator=Paginator(list_product,2)
    list_product=product_paginator.get_page(page)
    context={'products':list_product}
    return render(request,'product.html',context)

def Product_Details(request,pk):
    product_details=Product.objects.get(pk=pk)
    
    context={'product':product_details}
    return render(request,'products_details.html',context)
