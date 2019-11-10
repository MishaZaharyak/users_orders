from core.models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    birthdate = serializers.DateField(format='%d/%m/%Y')
    registration_date = serializers.DateField(format='%d/%m/%Y')

    class Meta:
        model = Customer
        exclude = ('order', )
