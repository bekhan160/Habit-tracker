from django.contrib.auth.models import AbstractUser
from django.db import models
from oauth2_provider.models import Application as OAuth2Application


class Application(OAuth2Application):
    class Meta(OAuth2Application.Meta):
        app_label = 'Habit tracker'


class Habit(models.Model):

    habit_name = models.CharField(max_length=30, unique=True)
    descriptions = models.CharField(max_length=60)
    target = models.IntegerField()
    frequency = models.IntegerField()
    start_day = models.DateField(auto_now=True)
    deadline = models.DateField()

    @classmethod
    def create_from_post(cls, data):
        instance = cls(
            habit_name=data['habit'],
            descriptions=data['descriptions'],
            target=data['target'],
            frequency=data['frequency'],
            deadline=data['deadline']
        )
        instance.save()
        return instance

    def __str__(self):
        return self.habit_name


class User(AbstractUser):

    habit_name = models.ManyToManyField(Habit, related_name='users')

    @classmethod
    def create_from_post(cls, data):

        instance = cls(password=data['password'], email=data['email'])
        instance.save()

        return instance



