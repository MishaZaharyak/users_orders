from django.urls import path
from core.views import (
    CustomersList,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    CustomersUploadCSVFile,
)

app_name = 'customer'

urlpatterns = [
    path('', CustomersList.as_view(), name='customers_list'),
    path('customer-form', CustomerCreateView.as_view(), name='customer_create'),
    path('customer-edit/<int:pk>', CustomerUpdateView.as_view(), name='customer_edit'),
    path('customer-delete/<int:pk>', CustomerDeleteView.as_view(), name='customer_delete'),
    path('upload-file', CustomersUploadCSVFile.as_view(), name='upload_file'),
]
