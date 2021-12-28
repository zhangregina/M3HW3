from django.shortcuts import render, redirect
from . import models, forms


def home_page(request):
    products = models.Product.objects.filter().order_by('-id')
    return render(request, 'home_page.html', {'product': products})
