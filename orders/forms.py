from django import forms
from .models import Order
from items.models import Item
from django.shortcuts import redirect,get_object_or_404
from django.core.exceptions import ValidationError

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'address']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity
    def form_valid(self, form):
        item_id = self.kwargs.get('pk')
        item = get_object_or_404(Item, pk=item_id)

        # Validate that requested quantity is not greater than available stock
        requested_quantity = form.cleaned_data['quantity']
        if requested_quantity > item.quantity:
            form.add_error('quantity', 'Requested quantity exceeds available stock.')
            return self.form_invalid(form)

        # Update stock and save order
        order = form.save(commit=False)
        order.item = item
        order.customer = self.request.user
        order.total_price = item.price * requested_quantity

        # Update item stock
        item.quantity -= requested_quantity
        item.save()

        # Save order
        order.save()
        return redirect('customer_home')
