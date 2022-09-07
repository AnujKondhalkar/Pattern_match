from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'base/home.html')


def check(request):

    str_in = request.GET['string']
    pattern_in = request.GET['pattern']
    result = str_in + pattern_in

    return render(request, 'base/output.html', {'Result': result})
