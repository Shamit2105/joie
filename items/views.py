from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Item
from .forms import ItemForm

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

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
