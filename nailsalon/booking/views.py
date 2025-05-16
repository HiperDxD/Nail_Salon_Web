from django.shortcuts import render
from .forms import AppointmentForm
from django.core.mail import send_mail
from django.conf import settings

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            #Email logic
            send_mail(
                'Confirmarea programarii tale',
                f'Multumesc pentru programare, {appointment.name}!',
                settings.DEFAULT_FROM_EMAIL,
                [appointment.email],
                fail_silently=False,
            )
            return redirect('success')
    else:
        form = AppointmentForm()
    return render(request, 'booking/book_appointment.html', {'form': form})   
