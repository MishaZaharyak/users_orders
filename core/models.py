from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    registration_date = models.DateField()
    order = models.OneToOneField('Order', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['registration_date']

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


@receiver(post_delete, sender=Customer)
def delete_related_order(sender, instance, **kwargs):
    instance.order.delete()


class Product(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Order(models.Model):
    created_date = models.DateField(auto_now=True)
    products = models.ManyToManyField(Product, related_name='products')

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        queryset = self.products.all()
        return ', '.join([str(product) for product in queryset])
