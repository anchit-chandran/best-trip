from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trips', views.list_trips, name='list_trips'),
    path('trips/<int:trip_id>', views.view_trip, name='view_trip')
]
