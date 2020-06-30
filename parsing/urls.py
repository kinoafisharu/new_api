from django.urls import path
from . import views

urlpatterns = [
    path(r'parsefilms/', views.FilmDotParseView.as_view(), name='parsefilms'),
]
