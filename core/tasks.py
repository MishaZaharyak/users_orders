from celery import shared_task
from core.utils import CustomReader
from datetime import datetime
from core.models import Customer


@shared_task
def create_customer(file):
    fieldnames = ['first_name', 'last_name', 'birthdate', 'registration_date']
    customers = CustomReader(file, fieldnames=fieldnames)

    for customer in customers:
        birthdate = datetime.strptime(customer.get('birthdate'), '%Y/%m/%d')
        registration_date = datetime.strptime(customer.get('registration_date'), '%Y/%m/%d')

        Customer.objects.get_or_create(
            first_name=customer.get('first_name', ''),
            last_name=customer.get('last_name', ''),
            birthdate=birthdate,
            registration_date=registration_date
        )
