from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("category/<str:category>", views.category, name = "category"),
    path("category/<str:category>/<int:dish_id>", views.dish, name = "dish"),
]