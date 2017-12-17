from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if hasattr(user, 'customer'):
            return True
        return False
