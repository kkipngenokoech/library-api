from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from.models import Book

# Create your views here.
def HomePage(request):
    return HttpResponse("Welcome to multiverse")


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    # template_name = 'book_list.html'
