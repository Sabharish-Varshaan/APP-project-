from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('active-tracking/', views.active_tracking, name='active_tracking'),
    path('health-monitoring/', views.health_monitoring, name='health_monitoring'),
    path('data-analysis/', views.data_analysis, name='data_analysis'),
    path('custom-workout/', views.custom_workout, name='custom_workout'),
]