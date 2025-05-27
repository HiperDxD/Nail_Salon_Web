from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    TIME_CHOICES = [(f"{h:02d}:00", f"{h:02d}:00") for h in range(10, 21)]  # 10:00 to 20:00
    time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'service', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'text',
                'placeholder': 'Select a date',
                'class': 'datepicker'  # optional, for better targeting
            })
        }