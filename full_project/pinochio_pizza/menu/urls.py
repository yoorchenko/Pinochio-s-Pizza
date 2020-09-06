from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("cart/", views.cart, name = "cart"),
    path("category/<str:category>", views.category, name = "category"),
    path("category/<str:category>/<int:dish_id>", views.dish, name = "dish"),
    path("category/<str:category>/<int:dish_id>/order", views.order, name = "order"),
]