from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "posts"

urlpatterns = [
    path('', views.PostList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
