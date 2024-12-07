from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Order
from items.models import Item
from .forms import OrderForm
from django.urls import reverse_lazy


class CustomerHomeView(LoginRequiredMixin, ListView):
    """Displays the list of items available for customers to order."""
    model = Item
    template_name = 'customer_home.html'
    context_object_name = 'items'

    def get_queryset(self):
        # Filter items that are in stock
        return Item.objects.filter(quantity__gt=0)


class PlaceOrderView(FormView):
    template_name = "place_order.html"
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('customer_home')  # Define redirection URL after successful order placement

    def form_valid(self, form):
        # Retrieve the item from the URL
        item_id = self.kwargs.get('pk')
        item = get_object_or_404(Item, pk=item_id)

        # Check quantity availability
        quantity = form.cleaned_data['quantity']
        if quantity > item.quantity:
            form.add_error('quantity', 'Requested quantity exceeds available stock.')
            return self.form_invalid(form)

        # Create order instance without saving to the database
        order = form.save(commit=False)

        # Assign item and customer after initial validation
        order.item = item
        order.customer = self.request.user
        order.total_price = item.price * quantity

        # Save the order to the database
        order.save()

        # Update item stock
        item.quantity -= quantity
        item.save()

        # Redirect to success page
        return super().form_valid(form)
