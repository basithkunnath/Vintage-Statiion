from django.urls import path
from . import views
urlpatterns = [
    path('product', views.Product_list, name='product'),
    path('product_details/<pk>', views.Product_Details, name='product_details'),
]


