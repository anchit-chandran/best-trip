from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trips', views.list_trips, name='list_trips'),
    path('trips/<int:trip_id>', views.view_trip, name='view_trip'),
    path('create-trip', views.TripReportCreateView.as_view(), name='create_trip'),
    path('trips/<int:trip_id>/edit', views.edit_trip, name='edit_trip')
]
