from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    sign_up,
    sign_confirm,
)


router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', sign_up),
    path('auth/token/', sign_confirm),
]
