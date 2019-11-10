from django.urls import path, include
from core.views import index

app_name = 'core'
urlpatterns = [
    path('', index),
    path('customers/', include('core.urls.customer')),
    path('orders/', include('core.urls.order')),
    path('products/', include('core.urls.product')),
]
