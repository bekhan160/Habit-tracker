
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserApiView, HabitApiView, SocialLoginView


urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserApiView.as_view(), name='user'),
    path('api/habit/', HabitApiView.as_view(), name='habit'),
    path('auth/register/', UserApiView.as_view(), name='register'),
    path('auth/login/google-oauth2/', SocialLoginView.as_view(), name='google'),
]




