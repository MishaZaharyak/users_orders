from django.urls import path
from core.views import (
    ProductsList,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = 'product'

urlpatterns = [
    path('', ProductsList.as_view(), name='products_list'),
    path('product-form', ProductCreateView.as_view(), name='product_create'),
    path('product-edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product-delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
