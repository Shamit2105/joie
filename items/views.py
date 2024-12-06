from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse  # new
from .models import Item
from .forms import ItemForm

class ItemListView(ListView):
    model = Item
    template_name = "item_list_seller.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail_seller.html"

class ItemCreateView(CreateView):
    model = Item
    template_name = "item_create_seller.html"
    fields = (
        "title",
        "description",
        "price",
        "quantity"
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)