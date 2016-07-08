from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_session(request):
    if 'click_cnt' in request.session:
        request.session['click_cnt'] += 1
    else:
        request.session['click_cnt'] = 1

    return HttpResponse('click_cnt = %d' % request.session['click_cnt'])
