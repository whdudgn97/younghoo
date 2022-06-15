from msilib.schema import ListView

from django.shortcuts import render
from django.views.generic import DetailView

from .models import Product
from .forms import RegisterForm
from django.views.generic.edit import FormView


class ProductRegister(FormView):
    template_name = 'product_register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            stock=form.data.get('stock'),
            description=form.data.get('description')
        )
        product.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()
    context_object_name = 'product'


class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
