from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.
def student(request):
    t = loader.get_template('student.html')
    c = Context({
        'title': 'student score list',
        'student': ['jimmy', 'tom', 'bob', 'rose'],
        'score':   [58,      100,   70,    50   ],
    })
    return HttpResponse(t.render(c))
