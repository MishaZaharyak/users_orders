from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, FormView, UpdateView, DeleteView, TemplateView
from core.models import Customer
from core.forms import CustomerForm
from django.shortcuts import redirect
from django.urls import reverse
from core.tasks import create_customer


def index(request):
    return redirect(reverse('core:customer:customers_list'))


class CustomersList(ListView):
    model = Customer
    paginate_by = 15
    template_name = 'customer/list.html'


class CustomerCreateView(FormView):
    template_name = 'customer/form.html'
    form_class = CustomerForm

    def post(self, request, *args, **kwargs):
        instance = None
        data = request.POST
        if 'pk' in data:
            instance = get_object_or_404(Customer, id=data['pk'])

        form = self.form_class(data, instance=instance)

        if form.is_valid():
            form.save()
            return JsonResponse({'result': 1, 'message': 'Customer successfully created'})
        else:
            return JsonResponse(
                {'result': -1, 'message': f'{form.errors}', 'errors': form.errors})


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/form.html'


class CustomerDeleteView(DeleteView):
    model = Customer

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        name = obj.get_full_name
        obj.delete()
        return JsonResponse({'result': 1, 'message': f'Customer {name} successfully deleted!'})


class CustomersUploadCSVFile(TemplateView):
    template_name = 'customer/upload_file.html'

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')

        if file.name.split(".")[-1] != 'csv':
            return JsonResponse({'result': -1, 'message': 'Only for type files: ".csv"'})

        try:
            create_customer.delay(file.read().decode())
            return JsonResponse({'result': 1, 'message': 'Customers successfully created'})
        except Exception as e:
            return JsonResponse({'result': -1, 'message': 'Server Error'})
