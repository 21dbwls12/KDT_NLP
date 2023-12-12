"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from Game import views


def home(request):
    return render(request, "index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    # game/을 주소에 붙이면 game.urls참조
    path("game/", include("Game.urls")),
    path('getImage/', views.getImagepage, name='getImage'),
    # 초기화면
    path("", home)
]
