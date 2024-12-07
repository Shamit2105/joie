
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path("seller_items/", include("items.urls")),
    path("customer_orders/",include("orders.urls")), 
    path('', include('pages.urls')),
]
