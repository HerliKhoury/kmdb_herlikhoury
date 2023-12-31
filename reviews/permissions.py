from rest_framework import permissions
from rest_framework.views import Request, View


class IsAllowedUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.is_critic
        return False