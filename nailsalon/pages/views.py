# pages/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def services(request):
    return render(request, 'pages/services.html')
