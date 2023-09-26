from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm
from .utils import get_book_image

# Create your views here.
class BookListView(ListView):
    model = Book
class BookDetailView(DetailView):
    model = Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        api_key = 'API_KEY'
        context['cover_url'] = get_book_image(self.object.title, api_key)
        return context
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_confirm_update'
    success_url = reverse_lazy('book_list')
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
