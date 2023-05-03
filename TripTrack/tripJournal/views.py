from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, TripReport

# Create your views here.
def index(request):
    return render(request, template_name='tripJournal/index.html')

def list_trips(request):
    trip_reports = TripReport.objects.all()
    
    return render(request, template_name='tripJournal/list_trips.html', context={'trip_reports':trip_reports})

def view_trip(request, trip_id):
    trip_report = TripReport.objects.get(id=trip_id)
    
    return render(request, template_name='tripJournal/view_trip.html', context={'trip_report':trip_report})


