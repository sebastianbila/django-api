from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from django.urls import include, path, re_path
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView

from .views import TokenObtainView

app_name = "authentication"

urlpatterns = [
    path('/login', TokenObtainView.as_view()),
    path('/token', TokenRefreshView.as_view()),
    path('/regisration', TokenRefreshView.as_view()),
]
