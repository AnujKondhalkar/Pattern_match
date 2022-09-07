from django.shortcuts import render
from django.http import HttpResponse
import re


def home(request):
    return render(request, 'base/home.html')


def check(request):

    str_in = request.GET['string']
    pattern_in = request.GET['pattern']

    if re.search(pattern_in, str_in):
        result = 'Yes'
    else:
        result = 'No'

    return render(request, 'base/output.html', {'Result': result})
