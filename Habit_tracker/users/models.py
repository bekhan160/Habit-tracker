from django.contrib.auth.models import AbstractUser
from django.db import models
from oauth2_provider.models import Application as OAuth2Application


class Application(OAuth2Application):
    class Meta(OAuth2Application.Meta):
        app_label = 'myapp'


class User(AbstractUser):

    @classmethod
    def create_from_post(cls, data):
        instance = cls(username=data['username'], password=data['password'], email=data['email'])
        instance.save()
        return instance


class Habit(models.Model):

    habit = models.CharField(max_length=30, unique=True)

    @classmethod
    def create_from_post(cls, data):
        instance = cls(habit=data['habit'])
        instance.save()
        return instance

    def __str__(self):
        return self.habit


class UsersHabit(models.Model):

    user = models.ForeignKey("User", on_delete=models.CASCADE)
    habit = models.ForeignKey("Habit", on_delete=models.CASCADE)




