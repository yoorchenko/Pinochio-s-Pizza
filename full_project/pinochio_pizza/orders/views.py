from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import Item, Order

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def place_order(request):
    new_order = Order(orderer_id = 4, total = request.session["total"])
    new_order.save()
    for item in request.session["cart"]:
        new_item = Item(name = item["item"], price = item["price"])
        new_item.save()
        new_order.items.add(new_item)
    total = request.session["total"]
    request.session["cart"] = []
    request.session["total"] = 0
    items = new_order.items.all()
    message = ""
    for item in items:
        message += f"{item} <br>"
    message += f"{total}$"
    context = {"total": 0}

    print(items)

    message = Mail(
        from_email='mihailstudent2601@gmail.com',
        to_emails='mihailstudent2601@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content=f'<strong>{ message }</strong>')
    try:
        sg = SendGridAPIClient('')
        response = sg.send(message)
    except Exception as e:
        print(e.message)





    return render(request, "menu/cart.html", context)


def signupview(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserCreationForm()
    return render(request, 'menu/signup.html', {'form': form})


def loginview(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "menu/login.html")
