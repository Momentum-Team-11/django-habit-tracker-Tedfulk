from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Habit(models.Model):
    habit = models.CharField(max_length=500)
    goal = models.CharField(max_length=500)
    user = models.ForeignKey(
        User, related_name="habits", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.habit


class Result(models.Model):
    record = models.ForeignKey(
        Habit, related_name="record", on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now_add=datetime.now)
    completed = models.BooleanField(default=False)
