from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, sign_confirm, sign_up

router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', sign_up),
    path('auth/token/', sign_confirm),
]
