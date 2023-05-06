from django import forms
from django.forms import ModelForm
from tripJournal.models import TripReport, Substance


class CreateTripReportForm(ModelForm):

    class Meta:
        model = TripReport
        fields = '__all__'
        widgets = {
            'datetime_of_trip': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'dosage': forms.NumberInput(attrs={'class': 'form-control'}),
            'dosage_units': forms.TextInput(attrs={'class': 'form-control'}),
            'substance': forms.Select(attrs={'class': 'form-control'}),
        }


class EditTripReportForm(ModelForm):

    class Meta:
        model = TripReport
        fields = '__all__'
