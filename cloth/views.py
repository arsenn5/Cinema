from django.views.generic import ListView, CreateView
from .models import Product, Order
from .forms import OrderForm
from django.shortcuts import render


class IndexView(ListView):
    model = Product
    template_name = 'cloth/index.html'
    context_object_name = 'products'


class ProductsByTagUniversalView(ListView):
    template_name = 'cloth/products_by_tag_universal.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(tags__name='универсальный')


class ProductsByTagMaleView(ListView):
    template_name = 'cloth/products_by_tag_male.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(tags__name='мужская')


class ProductsByTagFemaleView(ListView):
    template_name = 'cloth/products_by_tag_female.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(tags__name='женская')


class ProductsByTagChildrenView(ListView):
    template_name = 'cloth/products_by_tag_children.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(tags__name='детская')


class CreateOrderView(CreateView):
    form_class = OrderForm
    template_name = 'cloth/create_order.html'
    queryset = Order.objects.all()
    success_url = '/cloth/'

    def form_valid(self, form):
        return super(CreateOrderView, self).form_valid(form=form)
