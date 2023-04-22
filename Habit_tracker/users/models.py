from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Habit(models.Model):
    habit = models.CharField(max_length=30)

    def __str__(self):
        return self.habit
