from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_posts, name='book_view'),
    path('books/<int:id>/', views.book_detail, name='book_detail_view'),
]
