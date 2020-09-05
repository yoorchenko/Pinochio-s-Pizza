from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("category/<str:category>", views.category, name = "category"),
    path("category/<str:category>/<int:dish_id>", views.dish, name = "dish"),
    path("category/<str:category>/<int:dish_id>/size_change", views.size_change, name = "size_change"),
]