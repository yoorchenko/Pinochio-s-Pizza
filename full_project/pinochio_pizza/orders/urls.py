from django.urls import path
from . import views

urlpatterns = [
    path("", views.place_order, name = "confirm"),
    path("signup/", views.signupview, name = "signup"),
    path("login/", views.loginview, name = "login"),
]