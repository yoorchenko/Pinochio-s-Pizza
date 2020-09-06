from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Order

def place_order(request):
    new_order = Order(orderer_id = 4, total = request.session["total"])
    new_order.save()
    for item in request.session["cart"]:
        print(item["price"])
        new_item = Item(name = item["item"], price = item["price"])
        new_item.save()
        new_order.items.add(new_item)
    request.session["cart"] = []
    request.session["total"] = 0
    context = {"total": 0}
    return render(request, "menu/cart.html", context)
