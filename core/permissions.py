from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "You do not have permission to perform this action. It is not your account"

    def has_permission(self, request, view):
        permission = int(view.kwargs.get('pk')) == request.user.pk
        return True if permission else False


class IsSuperUser(permissions.BasePermission):
    message = "You don't have permission. To do this you need to be superuser"

    def has_permission(self, request, view):
        permission = request.user.is_superuser
        return True if permission else False
