from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic.edit import CreateView, UpdateView

from .models import Substance, TripReport

from .forms import EditTripReportForm

# Create your views here.
def index(request):
    return render(request, template_name='tripJournal/index.html')

def list_trips(request):
    trip_reports = TripReport.objects.all()
    
    return render(request, template_name='tripJournal/list_trips.html', context={'trip_reports':trip_reports})

def view_trip(request, trip_id):
    trip_report = TripReport.objects.get(id=trip_id)
    
    return render(request, template_name='tripJournal/view_trip.html', context={'trip_report':trip_report})

def edit_trip(request, trip_id):
    
    trip_report = get_object_or_404(TripReport, id=trip_id)
    
    if request.method == 'POST':
        form = EditTripReportForm(request.POST, instance=trip_report)
        if form.is_valid():
            form.save()
            return redirect('view_trip', trip_id=trip_id)
        else:
            return render(request, template_name='tripJournal/edit_trip.html',context={'form':form})
    
    elif request.method == 'GET':

        form = EditTripReportForm(instance=trip_report)
        
        return render(request, template_name='tripJournal/edit_trip.html', context={'form':form})
    

class TripReportCreateView(CreateView):
    model = TripReport
    fields = '__all__'
    template_name = 'tripJournal/create_trip_report.html'
    success_url = reverse_lazy('list_trips')

