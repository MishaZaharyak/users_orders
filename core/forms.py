from django import forms
from .models import Customer, Order, Product
from tempus_dominus.widgets import DatePicker
from django.contrib.postgres.forms import SimpleArrayField


class CustomerForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=DatePicker(
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            },
            options={
                'locale': 'uk',
                'icons': {
                    'date': 'fa fa-calendar',
                    'up': 'fa fa-arrow-up',
                    'down': 'fa fa-arrow-down',
                    'previous': 'fa fa-chevron-left',
                    'next': 'fa fa-chevron-right',
                    'today': 'fa fa-calendar-check-o',
                    'clear': 'fa fa-trash',
                    'close': 'fa fa-times'
                },
                'format': 'DD/MM/YYYY'
            }
        ),
        input_formats=['%d/%m/%Y'],
    )

    registration_date = forms.DateField(
        widget=DatePicker(
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            },
            options={
                'locale': 'uk',
                'icons': {
                    'date': 'fa fa-calendar',
                    'up': 'fa fa-arrow-up',
                    'down': 'fa fa-arrow-down',
                    'previous': 'fa fa-chevron-left',
                    'next': 'fa fa-chevron-right',
                    'today': 'fa fa-calendar-check-o',
                    'clear': 'fa fa-trash',
                    'close': 'fa fa-times',
                },
                'format': 'DD/MM/YYYY'
            },
        ),
        input_formats=['%d/%m/%Y'],
    )

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'birthdate', 'registration_date', 'order')


class OrderForm(forms.ModelForm):
    products = SimpleArrayField(forms.IntegerField(), min_length=1, delimiter=',')

    def save(self, commit=True):
        instance = super().save()
        instance.products.set(Product.objects.filter(id__in=self.cleaned_data['products']))
        return instance

    class Meta:
        model = Order
        fields = ('products', )


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name',)
