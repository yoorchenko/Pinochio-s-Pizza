from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Order
from telegram.ext import Updater
from django.conf import settings
from django.core.mail import send_mail

def place_order(request):
    new_order = Order(orderer_id = 4, total = request.session["total"])
    new_order.save()
    for item in request.session["cart"]:
        new_item = Item(name = item["item"], price = item["price"])
        new_item.save()
        new_order.items.add(new_item)
    request.session["cart"] = []
    request.session["total"] = 0
    context = {"total": 0}
    items = new_order.items.all()
    message = ""
    for item in items:
        message += f"{item} \n"
    message += f"{context['total']}$"

    print(items)

    send_mail(
        'Subject here',
        message,
        'mikhailyurchenko2601@gmail.com',
        ['mikhailyurchenko2601@gmail.com'],
        fail_silently=False,
    )
    return render(request, "menu/cart.html", context)
