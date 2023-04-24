
from django.urls import path, include
from users.views import UserApiView, HabitApiView, SocialLoginView


urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('register/', UserApiView.as_view(), name='register'),
    path('habit/', HabitApiView.as_view(), name='habit'),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('auth/google/', SocialLoginView.as_view(), name='google')
]




