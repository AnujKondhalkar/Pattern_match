from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def regex(request):
    return HttpResponse('Hey Regex')
