from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from core.models import Order, Product
from core.forms import OrderForm


class OrdersList(ListView):
    model = Order
    paginate_by = 15
    template_name = 'order/list.html'


class OrderCreateView(FormView):
    template_name = 'order/form.html'
    form_class = OrderForm

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'products': Product.objects.all()
        })
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        instance = None
        post_data = request.POST

        if 'pk' in post_data:
            instance = get_object_or_404(Order, id=post_data['pk'])

        form = self.form_class(post_data, instance=instance)

        if form.is_valid():
            form.save()
            return JsonResponse({'result': 1, 'message': 'Order successfully created'})
        else:
            return JsonResponse(
                {'result': -1, 'message': f'{form.errors}', 'errors': form.errors})


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'products': Product.objects.all()
        })
        return context


class OrderDeleteView(DeleteView):
    model = Order

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return JsonResponse({'result': 1, 'message': 'Order successfully deleted!'})
