from django.urls import path
from .views import (
    passenger_list, 
    passenger_create, 
    passenger_detail, 
    passenger_delete
)

urlpatterns = [
    # List all passengers
    path('', passenger_list, name='passenger_list'),
    
    # Create a new passenger
    path('create/', passenger_create, name='passenger_create'),
    
    # View a specific passenger's details
    path('<int:id>/', passenger_detail, name='passenger_detail'),
    
    # Delete a specific passenger
    path('<int:id>/delete/', passenger_delete, name='passenger_delete'),
]
