from rest_framework.generics import ListAPIView
from core.models import Customer
from .serializers import CustomerSerializer
from datetime import datetime


class CustomersApiListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        registration_date = self.request.query_params.get('registration_date', None)

        if registration_date:
            date = datetime.strptime(registration_date, '%d/%m/%Y')
            queryset = queryset.filter(registration_date=date)
        return queryset
