from django.conf.urls import include, url

from apps.core import routers

from . import views

app_name = "employees"

router = routers.BaseRouter()
router.register(r'^', views.EmployeeViewSet)

urlpatterns = [
    url('', include(router.urls))
]
