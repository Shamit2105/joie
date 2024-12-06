from django.urls import path
from .views import ItemDetailView,ItemListView,ItemCreateView

urlpatterns = [
    path("<int:pk>/",ItemDetailView.as_view(),name="item_detail_seller"),
    path("",ItemListView.as_view(),name="item_list_seller"),
    path("new_seller_item/", ItemCreateView.as_view(), name="item_create_seller"),
]
