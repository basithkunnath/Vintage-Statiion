from django import forms
from .models import OrderdItem
from .models import BillingInformation

class AddToCartForm(forms.ModelForm):
    class Meta:
        model = OrderdItem
        fields = ['product', 'quantity']


class BillingInformationForm(forms.ModelForm):
    class Meta:
        model = BillingInformation
        fields = ['address', 'city', 'state', 'postal_code', 'country', 'payment_method']