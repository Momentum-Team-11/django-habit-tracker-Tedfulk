from django.contrib import admin
from habit.models import Result, Habit

admin.site.register(Habit, Result)