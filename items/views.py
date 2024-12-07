from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .models import Item
from .forms import ItemForm
from django.urls import reverse_lazy


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "item_list_seller.html"

    def get_queryset(self):
        if self.request.user.is_seller:
            return Item.objects.filter(seller=self.request.user)
        return Item.objects.none()

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "item_detail_seller.html"

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = "item_create_seller.html"
    success_url = reverse_lazy('item_list')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin,UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "item_update_seller.html"

    def get_queryset(self):
        return Item.objects.filter(seller=self.request.user)
    
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "item_delete_seller.html"
    success_url = reverse_lazy('item_list')  # Redirect after deletion

    def get_queryset(self):
        return Item.objects.filter(seller=self.request.user)
