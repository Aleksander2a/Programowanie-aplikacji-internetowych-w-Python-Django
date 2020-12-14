from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, template_name="index.html") # dopisane

def form(request):
    return render(request, template_name="form.html") # dopisane
