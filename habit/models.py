from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Habit(models.Model):
    habit = models.CharField(max_length=500, null=True, blank=True)
    goal = models.CharField(max_length=500, null=True, blank=True)
    unit = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(
        User, related_name="habits", on_delete=models.CASCADE,
        null=True, blank=True)

    def __str__(self):
        return self.habit


class Result(models.Model):
    daily_record = models.IntegerField()
    update_date = models.DateField(default=datetime.now)
    completed = models.BooleanField(default=False)
    habit_record = models.ForeignKey(
        Habit, related_name="record", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.daily_record)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["habit_record", "update_date"], name="one_record_per_day")
        ]
