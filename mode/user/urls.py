from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("userSignup/", views.userSignup, name="userSignup"),
    path("userLogin/", views.userLogin, name="userLogin"),
]