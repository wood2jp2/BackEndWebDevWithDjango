from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def namastePage(request):
    return HttpResponse('Namaste means hello in Hindi.')