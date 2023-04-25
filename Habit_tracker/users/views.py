
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from social_core.exceptions import AuthForbidden
from social_django.utils import psa

from users.models import User, Habit
from users.serializers import UserSerializer, HabitSerializer


class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        instance = User.create_from_post(data)
        serializer = UserSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def post(self, request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #     email = request.data.get('email')
    #     habit_name = request.data.get('habit')
    #
    #     user = User(username=username, password=password, email=email, )
    #     user.save()
    #
    #     habit = Habit(habit=habit_name)
    #     habit.save()
    #
    #     user.habit.add(habit)
    #     user.save()
    #
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class HabitApiView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        instance = Habit.create_from_post(data)
        serializer = HabitSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SocialLoginView(TokenObtainPairView):
    @api_view(['POST'])
    @permission_classes([AllowAny])
    @psa('social:complete')
    def SocialLoginView(request, backend):
        try:
            user = request.backend.do_auth(request.data.get('access_token'))
        except AuthForbidden as e:
            return Response({'error': 'Не удалось авторизоваться через Google'}, status=status.HTTP_400_BAD_REQUEST)

        if user:
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)

            jwt_token = {
                'access': str(access_token),
                'refresh': str(refresh_token),
            }

            return Response(jwt_token, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Не удалось авторизоваться через Google'}, status=status.HTTP_400_BAD_REQUEST)