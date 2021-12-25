from django.shortcuts import render
from django.views.generic import ListView, FormView
from . import models, forms, parser
from django.http import HttpResponseRedirect



class FilmView(ListView):
    model = models.Series
    template_name = 'film_index.html'

    def get_queryset(self):
        return models.Series.objects.all()


class ParserSeriesView(FormView):
    template_name = 'parser.html'
    form_class = forms.ParserForm
    success_url = '/series/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserSeriesView, self).post(request, *args, **kwargs)













