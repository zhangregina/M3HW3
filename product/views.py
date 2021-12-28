from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views.generic import ListView, FormView, CreateView, DetailView


class HomePage(ListView):
    model = models.Product_in
    template_name = 'home_page_in.html'

    def get_queryset(self):
        return models.Product_in.objects.filter().order_by('-id')


class OrderCreateView(CreateView):
    template_name = 'order_in.html'
    queryset = models.Order_in.objects.all()
    form_class = forms.OrderForm
    success_url = '/order/'

    def form_valid(self, form):
        return super().form_valid(form=form)


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Product_in, id=product_id)


class CustomerCreateView(CreateView):
    template_name = 'customer_in.html'
    queryset = models.Customer_in.objects.all()
    form_class = forms.CustomerForm
    success_url = '..'

    def form_valid(self, form):
        return super().form_valid(form=form)