from django.urls import path

from . import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("certificate/", views.certificate_view, name="certificate"),
]
