from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from users.models import User, Habit
from users.serializers import UserSerializer, HabitSerializer


# @api_view(['GET', 'POST'])
class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HabitApiView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer



# Django view а нам нужна DRF view

class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
        elif not form.is_valid():
            return UserCreationForm.error_messages

        context = {
            'form': form
        }
        return render(request, self.template_name, context)
