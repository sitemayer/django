from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.
def base(request):
    t = loader.get_template('base.html')
    c = Context({})
    return HttpResponse(t.render(c))

def home(request):
    t = loader.get_template('home.html')
    c = Context({})
    return HttpResponse(t.render(c))

def index(request):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))
