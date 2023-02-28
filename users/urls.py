from django.urls import path
from .views import AccountView, AccountDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("users/", AccountView.as_view()),
    path("users/<int:user_id>/", AccountDetailView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/refresh/", TokenRefreshView.as_view()),
]
