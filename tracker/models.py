from django.db import models
from django.contrib.auth.models import User

class ActiveTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    workout_type = models.CharField(max_length=10)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    stress_level = models.IntegerField()  # 1-10 scale
    hydration_level = models.IntegerField()  # 1-10 scale

class HealthMonitoring(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    sleep_time = models.IntegerField()  # in minutes
    heart_rate = models.IntegerField()
    blood_pressure_systolic = models.IntegerField()
    blood_pressure_diastolic = models.IntegerField()
    weight = models.FloatField()

class CustomWorkout(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)

    def __str__(self):
        return self.name