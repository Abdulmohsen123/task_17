from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "User is not the owner of this restaurant"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.is_staff:
            return True
        return False