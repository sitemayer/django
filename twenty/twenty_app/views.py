from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.template import loader

# Create your views here.
def index(request):
    tmp = _("Hello world")
    return HttpResponse(tmp)

def test(request):
    t = loader.get_template("test.html")
    return HttpResponse(t.render({'person': 'tony'}))
