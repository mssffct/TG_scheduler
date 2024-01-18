from rest_framework import permissions


class IsCreator(permissions.BasePermission):
    def has_permission(self, request, view):
        instance = view.get_object()
        #TODO check if user is creator of object
        return bool(
            request.app_user and instance
        )
