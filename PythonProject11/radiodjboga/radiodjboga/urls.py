from django.contrib import admin
from django.urls import path
from . import views   # Импортируем наши view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.player_page, name='home'),  # Это главная страница!
]