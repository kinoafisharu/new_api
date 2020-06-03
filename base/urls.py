from django.urls import path, include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()


# В регулярной строке (first arg) прописаны названия paths в апи (r'films', r'bananas', etc.)

# Все адреса роутера связаны по цепочке с - Views => Serializers => Models
# Нужны для регистрации структур апи в роутере который в свою очередь отдает ее в urlpatterns

# Отображение короткого описания фильмов в листе  (all fields) и длинного при детальном рассмотре фильма
router.register(r'films', views.FilmsViewSet, basename = 'films')
router.register(r'news', views.NewsViewSet, basename = 'news')
# -/ Александр Караваев

# router.register(r'persons', views.BasePersonViewSet)



urlpatterns = [
    # Включение корневого роутера в список URLS
    re_path(r'^', include(router.urls)),
    path('films/<int:pk>/like/', views.FilmsViewSet.as_view({"post": "like"})),
    # -/ Александр Караваев
]
