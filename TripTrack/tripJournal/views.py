from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Substance, TripReport

from .forms import (
    CreateTripReportForm,
     EditTripReportForm,
     UserLoginForm,
    )

def index(request):
    return render(request, template_name='tripJournal/index.html')

def list_trips(request):
    trip_reports = TripReport.objects.all()
    
    return render(request, template_name='tripJournal/list_trips.html', context={'trip_reports':trip_reports})

@login_required
def view_trip(request, trip_id):
    trip_report = TripReport.objects.get(id=trip_id)
    
    return render(request, template_name='tripJournal/view_trip.html', context={'trip_report':trip_report})

@login_required
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
    

@login_required
def create_trip(request):
    
    if request.method == 'GET':
        
        form = CreateTripReportForm()
        
        return render(request, template_name='tripJournal/create_trip_report.html', context={'form':form})
    
    elif request.method == 'POST':
        
        form = CreateTripReportForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('list_trips')
        

# AUTHENTICATION VIEWS
class CustomLoginFormView(LoginView):
    template_name = 'registration/login.html'
    success_url = 'home'
    
    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f'Welcome {user}! Happy tripping, friend 🔮')
        return super().form_valid(form)
    
# def login_user(request):
    
#     form = UserLoginForm()
    
#     if request.method == 'GET':
#         return render(request, template_name='registration/login.html', context={'form' : form})
    
#     elif request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         user = authenticate(
#             username=username,
#             password=password
#         )
        
#         if user is None:
#             messages.error(request, message='Log in unsucessful. Please check your username or password.')
#             return render(request, template_name='registration/login.html', context={'form' : form})
    
#         login(request, user)
#         messages.success(request, message = "<strong>EXCITING</strong> - you've logged in! Happy tripping! 🔮", extra_tags='safe')
        
#         return redirect('list_trips')

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, message='Successfully logged out. <b>Happy travels!</b> 👋🏽', extra_tags='safe')
    return redirect('home')