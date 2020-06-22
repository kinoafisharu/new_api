from django.urls import path
from . import views

urlpatterns = [
    path(r'parsefilms/', views.FilmParseView.as_view(), name='parsefilms'),
]
