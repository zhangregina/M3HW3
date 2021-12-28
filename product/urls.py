from django.urls import path
from . import views


urlpatterns = [
    path('product/', views.HomePage.as_view(), name='home_page_url'),
    path('order/', views.OrderCreateView.as_view(), name='order_url'),
    path('customer/', views.CustomerCreateView.as_view(), name='customer'),
    path('<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),





]