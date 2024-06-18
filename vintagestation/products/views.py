from django.shortcuts import render

# Create your views here.

def Product(request):
    return render(request,'product.html')