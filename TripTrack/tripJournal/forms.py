from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from tripJournal.models import TripReport, Substance


class CreateTripReportForm(ModelForm):
    class Meta:
        model = TripReport
        fields = "__all__"
        widgets = {
            "datetime_of_trip": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                    "aria-describedby": "datetimeOfTrip",
                }
            ),
            "location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Basel, Switzerland"}
            ),
            "dosage": forms.NumberInput(attrs={"class": "form-control"}),
            "dosage_units": forms.TextInput(attrs={"class": "form-control"}),
            "substance": forms.Select(
                attrs={"class": "form-control", "help_text": "Don't see your magic?"}
            ),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder":"A space to record any of your thoughts, feelings, or insights..."}),
        }


class EditTripReportForm(ModelForm):
    class Meta:
        model = TripReport
        fields = "__all__"
        widgets = {
            "datetime_of_trip": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "dosage": forms.NumberInput(attrs={"class": "form-control"}),
            "dosage_units": forms.TextInput(attrs={"class": "form-control"}),
            "substance": forms.Select(attrs={"class": "form-control"}),
        }

class AddSubstanceForm(ModelForm):
    
    class Meta:
        model = Substance
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={"class": "form-control"})
        }

# AUTHENTICATION FORMS
class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'})
        }


class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Enter your password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Confirm your password'}),
    )

    class Meta:
        model = User
        fields = ['username']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Enter your username'}),
        }