from django.urls import path
from .views import CustomersApiListView

app_name = 'api_customer'
urlpatterns = [
    path('customers', CustomersApiListView.as_view(), name='customers'),
]
