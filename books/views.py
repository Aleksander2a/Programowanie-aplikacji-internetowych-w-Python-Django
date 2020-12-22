from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

# Create your views here.

def main(request):
    return render(request, template_name="index.html") # dopisane

def form(request):
    return render(request, template_name="form.html") # dopisane

def books_list(request):
    books = Book.objects.all()
    return render(request, template_name="books_list.html", context={"books": books}) # dopisane
