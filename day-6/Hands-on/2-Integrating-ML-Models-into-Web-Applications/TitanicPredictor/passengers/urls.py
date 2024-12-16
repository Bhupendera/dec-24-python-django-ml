from django.urls import path
from .views import passenger_list, passenger_create, passenger_detail, passenger_delete

urlpatterns = [
    path('', passenger_list, name='passenger_list'),  # List all passengers
    path('create/', passenger_create, name='passenger_create'),  # Create a new passenger
    path('<int:id>/', passenger_detail, name='passenger_detail'),  # View a specific passenger
    path('<int:id>/delete/', passenger_delete, name='passenger_delete'),  # Delete a specific passenger
]
