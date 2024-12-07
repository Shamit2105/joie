from django import forms
from .models import Order
from items.models import Item

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'address']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity
