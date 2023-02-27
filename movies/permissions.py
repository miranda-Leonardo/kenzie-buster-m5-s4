from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Movie


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        try:
            return request.user.is_employee
        except AttributeError as err:
            return False
