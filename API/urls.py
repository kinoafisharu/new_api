from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('kinoinfo/', include('kinoinfo.urls')),
    path('texts/', include('textprod.urls')),
    path('sounds/', include('soundprod.urls')),
    path('process/', include('products.urls')),
    path('', views.index, name = 'index')
]
