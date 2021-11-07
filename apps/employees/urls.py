from core import routers
from django.conf.urls import include, url

from . import views

app_name = "employees"

router = routers.BaseRouter()
router.register(r'^', views.EmployeeViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
