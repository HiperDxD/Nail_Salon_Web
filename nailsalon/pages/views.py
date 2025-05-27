# pages/views.py

from django.shortcuts import render, get_object_or_404
from booking.models import Service

def home(request):
    return render(request, 'pages/home.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'pages/services.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'pages/service_detail.html', {'service': service})


