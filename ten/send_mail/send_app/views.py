from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
def send(request):
    send_mail('mail_test', 'this is test message', 'sitemayerlee@163.com', ['1151542547@qq.com'], fail_silently=True)
    return HttpResponse('refresh this page to send a test email')
