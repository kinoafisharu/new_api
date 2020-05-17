from django.urls import path, include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'films', views.BaseFilmsViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]
