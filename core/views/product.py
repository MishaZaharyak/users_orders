from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from core.models import Product
from core.forms import ProductForm


class ProductsList(ListView):
    model = Product
    paginate_by = 15
    template_name = 'product/list.html'


class ProductCreateView(FormView):
    template_name = 'product/form.html'
    form_class = ProductForm

    def post(self, request, *args, **kwargs):
        instance = None
        data = request.POST
        if 'pk' in data:
            instance = get_object_or_404(Product, id=data['pk'])

        form = self.form_class(data, instance=instance)

        if form.is_valid():
            form.save()
            return JsonResponse({'result': 1, 'message': 'Product successfully created'})
        else:
            return JsonResponse(
                {'result': -1, 'message': f'{form.errors}', 'errors': form.errors})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/form.html'


class ProductDeleteView(DeleteView):
    model = Product

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        name = obj.name
        obj.delete()
        return JsonResponse({'result': 1, 'message': f'Product {name} successfully deleted!'})
