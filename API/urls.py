from django.urls import path, include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()


# В регулярной строке (first arg) прописаны названия paths в апи (r'films', r'bananas', etc.)

# Все адреса роутера связаны по цепочке с - Views => Serializers => Models
# Нужны для регистрации структур апи в роутере который в свою очередь отдает ее в urlpatterns

# Отображение короткого описания фильмов в листе  (all fields) и длинного при детальном рассмотре фильма
router.register(r'films', views.BaseFilmsViewSet, basename = 'films')
# -/ Александр Караваев

# Отображение короткого описания фильмов в листе (restricted fields)
router.register(r'brieffilms', views.ShortBaseFilmsViewSet, basename = 'brieffilms')
# -/ Александр Караваев


urlpatterns = [
    # Включение корневого роутера в список URLS
    re_path(r'^', include(router.urls))
    # -/ Александр Караваев
]
