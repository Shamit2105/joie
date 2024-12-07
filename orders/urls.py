from django.urls import path
from .views import CustomerHomeView, PlaceOrderView

urlpatterns = [
    path('', CustomerHomeView.as_view(), name='customer_home'),
    path('place_order/<int:pk>/', PlaceOrderView.as_view(), name='place_order'),
]
