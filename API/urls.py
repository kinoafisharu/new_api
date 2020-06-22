from django.urls import path, include, re_path
from . import views

# Паттерны всех разделов API собраны Здесь
# Данный модуль используется как точка сборки ля всех частей и потмо отправляется в _main
urlpatterns = [
    path('kinoinfo/', include('kinoinfo.urls')),
    path('texts/', include('textprod.urls')),
    path('sounds/', include('soundprod.urls')),
    path('process/', include('products.urls')),
    path('parsing/', include('parsing.urls')),
    path('', views.index, name = 'index'),
]
