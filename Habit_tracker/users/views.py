
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from social_core.exceptions import AuthForbidden
from social_django.utils import psa
from users.models import User, Habit
from users.serializers import UserSerializer, HabitSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        instance = User.create_from_post(data)
        serializer = UserSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HabitApiView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        instance = Habit.create_from_post(data)
        serializer = HabitSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SocialLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def get_tokens_for_user(user):
        access_token = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user)

        return {
            'access': str(access_token),
            'refresh': str(refresh_token),
        }

    @psa('social:complete')
    def post(self, request, backend):
        try:
            user = request.backend.do_auth(request.POST.get('access_token'))
        except AuthForbidden as e:
            return Response({'error': 'Не удалось авторизоваться через Google'}, status=status.HTTP_400_BAD_REQUEST)

        if user:
            jwt_token = self.get_tokens_for_user(user)
            return Response(jwt_token, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Не удалось авторизоваться через Google'}, status=status.HTTP_400_BAD_REQUEST)

