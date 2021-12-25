from django.urls import path, include
from . import views
from django.contrib import admin
urlpatterns = [
    path('series/', views.FilmView.as_view(), name='series_view'),
    path('parser/', views.ParserSeriesView.as_view(), name='parser_view'),
]