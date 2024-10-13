from django.contrib import admin
from .models import ActiveTracking, HealthMonitoring, CustomWorkout

admin.site.register(ActiveTracking)
admin.site.register(HealthMonitoring)
admin.site.register(CustomWorkout)