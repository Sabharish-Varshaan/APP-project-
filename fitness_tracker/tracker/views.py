from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, ActiveTrackingForm, HealthMonitoringForm
from .models import ActiveTracking, HealthMonitoring, CustomWorkout
from django.db.models import Avg
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db.models.functions import TruncDate

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def active_tracking(request):
    if request.method == 'POST':
        form = ActiveTrackingForm(request.POST)
        if form.is_valid():
            tracking = form.save(commit=False)
            tracking.user = request.user
            tracking.save()
            messages.success(request, 'Workout tracked successfully!')
            return redirect('active_tracking')
    else:
        form = ActiveTrackingForm()
    return render(request, 'active_tracking.html', {'form': form})

@login_required
def health_monitoring(request):
    if request.method == 'POST':
        form = HealthMonitoringForm(request.POST)
        if form.is_valid():
            monitoring = form.save(commit=False)
            monitoring.user = request.user
            monitoring.save()
            messages.success(request, 'Health data recorded successfully!')
            return redirect('health_monitoring')
    else:
        form = HealthMonitoringForm()
    return render(request, 'health_monitoring.html', {'form': form})
@login_required
def data_analysis(request):
    calories_data = list(ActiveTracking.objects.filter(user=request.user)
                     .annotate(truncated_date=TruncDate('date'))
                     .values('truncated_date')
                     .annotate(value=Avg('calories_burned'))
                     .order_by('truncated_date'))

    sleep_data = list(HealthMonitoring.objects.filter(user=request.user)
                  .annotate(truncated_date=TruncDate('date'))
                  .values('truncated_date')
                  .annotate(value=Avg('sleep_time'))
                  .order_by('truncated_date'))

    heart_rate_data = list(HealthMonitoring.objects.filter(user=request.user)
                       .annotate(truncated_date=TruncDate('date'))
                       .values('truncated_date')
                       .annotate(value=Avg('heart_rate'))
                       .order_by('truncated_date'))
    
    def rename_key(data_list, old_key, new_key):
        return [{new_key if k == old_key else k: v for k, v in d.items()} for d in data_list]

    calories_data = rename_key(calories_data, 'truncated_date', 'date')
    sleep_data = rename_key(sleep_data, 'truncated_date', 'date')
    heart_rate_data = rename_key(heart_rate_data, 'truncated_date', 'date')

    context = {
    'calories_data': json.dumps(calories_data, cls=DjangoJSONEncoder),
    'sleep_data': json.dumps(sleep_data, cls=DjangoJSONEncoder),
    'heart_rate_data': json.dumps(heart_rate_data, cls=DjangoJSONEncoder),
}
    return render(request, 'data_analysis.html', context)

@login_required
def custom_workout(request):
    workouts = CustomWorkout.objects.all()
    context = {
        'workouts': workouts,
    }
    return render(request, 'custom_workout.html', context)