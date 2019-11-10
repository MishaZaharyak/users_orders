from django.urls import path
from core.views import (
    OrdersList,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView
)

app_name = 'order'

urlpatterns = [
    path('', OrdersList.as_view(), name='orders_list'),
    path('order-form', OrderCreateView.as_view(), name='order_create'),
    path('order-edit/<int:pk>', OrderUpdateView.as_view(), name='order_edit'),
    path('order-delete/<int:pk>', OrderDeleteView.as_view(), name='order_delete'),
]
