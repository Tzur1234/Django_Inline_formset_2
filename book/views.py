from django.shortcuts import render
from .models import Book, Author
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from django.utils import timezone

class HomeView(TemplateView):
    # TemplateResponseMixin (attribute)
    template_name = 'home.html'

class AuthorListView(ListView):
    model = Author
    template_name = "author_list.html"
    context_object_name = 'data' 

class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'

    # # ContentMixin
    # def get_context_data(self, )