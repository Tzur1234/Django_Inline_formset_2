from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book, Author
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.utils import timezone
from .forms import AuthorBooksFormset

from core import settings
from django.core.mail import send_mail

import environ
env = environ.Env()
environ.Env.read_env()

class HomeView(TemplateView):
    # TemplateResponseMixin (attribute)
    template_name = 'home.html'

class AuthorListView(ListView):
    model = Author
    template_name = "author_list.html"
    context_object_name = 'data' 

class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author 

class AuthorCreateView(CreateView):
    template_name= 'author_add.html'
    model = Author
    fields =['name',]

    def form_valid(self, form):

        messages.success(self.request,'The author has been added')

        return super().form_valid(form)    


class AuthorBookEditView(SingleObjectMixin, FormView):
    model = Author
    template_name = 'author_books_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return AuthorBooksFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('books:author_detail', kwargs={'pk': self.object.pk})




def index(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        content = request.POST['content']
        sender = request.POST['from_email']

        send_mail(
            subject,
            content,
            sender,
            [env('RECIEVERS')]
        )
        return render(request, 'contact_email.html', {'message': 'thanks the email was send !'})
    else:
        return render(request, 'contact_email.html')