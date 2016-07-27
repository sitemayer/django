from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    t = loader.get_template('home.html')
    return HttpResponse(t.render({}))

def case(request):
    t = loader.get_template('case.html')
    return HttpResponse(t.render({}))

def about(request):
    t = loader.get_template('about.html')
    return HttpResponse(t.render({}))
