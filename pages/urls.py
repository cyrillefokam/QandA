from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("generator", views.generator, name="generator"),
    path("about/", views.about, name="about"),
]
