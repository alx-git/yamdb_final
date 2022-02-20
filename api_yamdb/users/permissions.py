from django.contrib.auth import get_user_model
from rest_framework.permissions import SAFE_METHODS, BasePermission

User = get_user_model()


def isauthenticated(function):
    def wrapper(self, request=None, object=None):
        if not request.user.is_authenticated:
            return False
        return function(self, request, object)
    return wrapper


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return obj.author == request.user


class IsAdminOrSuper(BasePermission):

    @isauthenticated
    def check_permission(self, request, object):
        return (
            request.user.is_admin
            or request.user.is_superuser)

    def has_permission(self, request, view):
        return self.check_permission(request)

    def has_object_permission(self, request, view, obj):
        return self.check_permission(request=request, object=obj)


class IsModerator(BasePermission):

    @isauthenticated
    def check_permission(self, request, object):
        return request.user.is_moderator

    def has_permission(self, request, view):
        return self.check_permission(request)

    def has_object_permission(self, request, view, obj):
        return self.check_permission(request=request, object=obj)
