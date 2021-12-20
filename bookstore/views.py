from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.http import Http404
from django.views import generic


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


class BookCreateView(generic.CreateView):
    template_name = 'add_book.html'
    form_class = forms.BookForm
    success_url = '/books/'
    queryset = models.Book.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)


class BookUpdateView(generic.UpdateView):
    template_name = 'add_book.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)


class BookDeleteView(generic.DeleteView):
    template_name = 'book_delete.html'
    success_url = '/books/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=post_id)

# def get_posts(request, book=None):
#     book = models.Book.objects.all()
#     return render(request, 'book_list.html', {'book': book})
#
# def book_detail(request, id):
#     try:
#         book = models.Book.objects.get(id=id)
#         try:
#             comment = models.Comment.objects.filter(post_id=id).order_by('created_date')
#         except models.Comment.DoesNowExist:
#             return HttpResponse('No comments.')
#
#     except models.Book.DoesNotExist:
#         raise Http404(' This book does not exist')
#
#     return render(request, 'book_detail.html', {'book': book, 'book_comment' : comment})
#
#
# def add_book(request):
#     method = request.method
#     if method == "POST":
#         form = forms.BookForm(request.POST, request.FILES)
#         print(form.data)
#         models.Book.objects.create(title=form.data['title'],
#                                    description=form.data['description'],
#                                    image=form.data['image'])
#         return HttpResponse('Post created successfully.')
#     else:
#         form = forms.BookForm()
#
#     return render(request, 'add_book.html', {'form': form})
#
# def add_comment(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.CommentForm(request.POST, request.FILES)
#         print(form.data)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Comment created successfully!!!')
#     else:
#         form = forms.CommentForm()
#     return render(request, 'add_comment.html', {'form': form})
