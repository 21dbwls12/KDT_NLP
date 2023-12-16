from django.urls import path
from . import views

urlpatterns = [
    # path("", views.gamepage, name="gamepage"),
    path("", views.gamestart, name="gamestart"),
    path("getImage/", views.getImagepage, name="getImage"),
    path("fortest", views.fortest, name="fortest"),
    path("datatest", views.datatest, name="datatest"),
    path("mediatest", views.mediatest, name="mediatest"),
    path("category", views.category, name="category"),
    # path("gamestart", views.gamestart, name="gamestart"),
]