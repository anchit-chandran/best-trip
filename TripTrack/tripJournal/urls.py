from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trips', views.list_trips, name='list_trips'),
    path('trips/<int:trip_id>', views.view_trip, name='view_trip'),
    path('trips/create', views.create_trip, name='create_trip'),
    path('trips/<int:trip_id>/edit', views.edit_trip, name='edit_trip'),
    path('login', views.CustomLoginFormView.as_view(),name='login'),
    path('logout', views.logout_user, name='logout'),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path('add-substance', views.add_substance, name='add_substance')
]
