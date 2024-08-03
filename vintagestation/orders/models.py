from django.db import models
from customers.models import Customer
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    ORDER_CHOICE=((ORDER_PROCESSED,'ORDER_PROCESSED'),
                  (ORDER_DELIVERED,'ORDER_DELIVERED'),
                  (ORDER_REJECTED,'ORDER_REJECTED'))
    
    order_status=models.IntegerField(choices=ORDER_CHOICE,default=CART_STAGE)
    owner= models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

class OrderdItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='added_items')
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')


    def __str__(self):
        return self.title  
    


class BillingAddress(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f'{self.customer.username} - {self.address_line_1}, {self.city}, {self.country}'