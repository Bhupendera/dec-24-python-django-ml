from django.urls import path
from . import views

urlpatterns = [
    path('', views.passenger_list, name='passenger_list'),
    path('<int:pk>/', views.passenger_detail, name='passenger_detail'),  # Use 'pk' as the parameter name
    path('<int:pk>/delete/', views.passenger_delete, name='passenger_delete'),  # Add this
    path('create/', views.create_passenger, name='create_passenger'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
