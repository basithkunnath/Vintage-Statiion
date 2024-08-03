from django import forms
from .models import OrderdItem
from .models import BillingAddress

class AddToCartForm(forms.ModelForm):
    class Meta:
        model = OrderdItem
        fields = ['product', 'quantity']


class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['address_line_1','address_line_2','city','state','postal_code','country']
