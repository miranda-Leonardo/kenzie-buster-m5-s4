from rest_framework import permissions
from rest_framework.views import Request, View


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        try:
            return request.user.is_employee
        except AttributeError:
            return False
