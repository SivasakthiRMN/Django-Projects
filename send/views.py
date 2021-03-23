from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def view_func(request):
    send_mail('Hello from Sivasakthi',
    'Hello boy.This is an automated message',
    'Sivasakthiraman106@gmail.com',
    ['kapil30852@990ys.com'],
    fail_silently=False)
    return render (request,'send/index.html')
