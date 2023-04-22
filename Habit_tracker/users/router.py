
from rest_framework import routers

from users.views import UserApiView, HabitApiView

router = routers.DefaultRouter()

router.register(r'users', UserApiView)
router.register(r'habit/', HabitApiView, 'habit')


urlpatterns = router.urls
