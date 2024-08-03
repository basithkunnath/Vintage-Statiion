from django.shortcuts import render
from products . models import Product

# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('priority')[:3]
    context = {'featured_products': featured_products}
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')