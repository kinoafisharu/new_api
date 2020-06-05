
from django.contrib import admin
from django.urls import path, include

# -/ Александр Караваев
# Забирает все значения модулей urls из общего значения в  API.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('API.urls')),
]
