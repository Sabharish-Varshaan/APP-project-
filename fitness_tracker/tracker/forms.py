from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ActiveTracking, HealthMonitoring

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ActiveTrackingForm(forms.ModelForm):
    class Meta:
        model = ActiveTracking
        fields = ['date', 'workout_type', 'duration', 'calories_burned', 'stress_level', 'hydration_level']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'workout_type': forms.Select(choices=[('running', 'Running'), ('cardio', 'Cardio'), ('yoga', 'Yoga'), ('jogging', 'Jogging'), ('personal', 'Personal Workout')]),
        }

class HealthMonitoringForm(forms.ModelForm):
    class Meta:
        model = HealthMonitoring
        fields = ['date', 'sleep_time', 'heart_rate', 'blood_pressure_systolic', 'blood_pressure_diastolic', 'weight']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }