from django.urls import path
from .views import OrderView, PlaceOrderView

urlpatterns = [
    path('orders/', OrderView.as_view(), name='order-list'),
    path('orders/<int:order_id>/', OrderView.as_view(), name='order-detail'),
    path('place-order/', PlaceOrderView.as_view(), name='place-order'),
]
