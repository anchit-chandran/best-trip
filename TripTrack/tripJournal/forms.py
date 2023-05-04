from django.forms import ModelForm
from tripJournal.models import TripReport


class EditTripReportForm(ModelForm):
    
    class Meta:
        model = TripReport
        fields = '__all__'