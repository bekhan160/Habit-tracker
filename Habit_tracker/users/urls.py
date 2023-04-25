
from django.urls import path, include
from users.views import UserApiView, HabitApiView, SocialLoginView


urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('api/user/', UserApiView.as_view(), name='user'),
    path('api/habit/', HabitApiView.as_view(), name='habit'),
    path('auth/register/', UserApiView.as_view(), name='register'),
    path('auth/login/google-oauth2/', SocialLoginView.as_view(), name='google'),
]




