from django.urls import path, include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()


# В регулярной строке (first arg) прописаны названия paths в апи (r'films', r'bananas', etc.)

# Все адреса роутера связаны по цепочке с - Views => Serializers => Models
# Нужны для регистрации структур апи в роутере который в свою очередь отдает ее в urlpatterns

# Отображение короткого описания историй в листе
router.register(r'stories', views.StoriesViewSet, basename = 'stories')
# -/ Александр Караваев

# router.register(r'persons', views.BasePersonViewSet)

urlpatterns = [
    # Включение корневого роутера в список URLS
    re_path(r'^', include(router.urls)),
    # -/ Александр Караваев
]
