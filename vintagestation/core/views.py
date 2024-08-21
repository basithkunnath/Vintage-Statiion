from django.shortcuts import render
from products . models import Product

# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('priority')[:6]
    context = {'featured_products': featured_products}
    return render(request, 'index.html',context)

def related(request):
    related_products = Product.objects.order_by('priority')[:-6]
    context = {'related_products': related_products}
    return render(request, 'products_details.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def view_profile(request):
    return render(request, 'user_profile.html')