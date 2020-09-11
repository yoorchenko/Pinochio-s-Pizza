from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Regular_Pizza, Topping, Sicilian_Pizza, Sub, Extra_Sub, Pasta, Salad, Dinner_Platter

def index(request):
    print(request.user)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "menu/index.html")

def category(request, category):

    if category == "regular":
        context = {
            "category": category,
            "items": Regular_Pizza.objects.all(),
            }
    elif category == "sicilian":
        context = {
            "category": category,
            "items": Sicilian_Pizza.objects.all(),
            }
    elif category == "subs":
        context = {
            "category": category,
            "items": Sub.objects.all(),
            }
    elif category == "other":
        context = {
            "category": category,
            "pastas": Pasta.objects.all(),
            "salads": Salad.objects.all(),
            "dinner_platters": Dinner_Platter.objects.all(),
            }

    return render(request, "menu/category.html", context)

def dish(request, category, dish_id):
    if category == "regular":
        context = {
            "result": Regular_Pizza.objects.get(id=dish_id),
            "adds": Topping.objects.all(),
            "category": category,
        }
    elif category == "sicilian":
        context = {
            "result": Sicilian_Pizza.objects.get(id=dish_id),
            "adds": Topping.objects.all(),
            "category": category,
        }
    elif category == "subs":
        context = {
            "result": Sub.objects.get(id=dish_id),
            "adds": Extra_Sub.objects.all(),
            "category": category,
        }
    elif category == "salad":
        context = {
            "result": Salad.objects.get(id=dish_id),
            "category": category,
        }
    elif category == "pasta":
        context = {
            "result": Pasta.objects.get(id=dish_id),
            "category": category,
        }
    elif category == "dinner_platter":
        context = {
            "result": Dinner_Platter.objects.get(id=dish_id),
            "category": category,
        }

    return render(request, "menu/dish.html", context)

def order(request, category, dish_id):
    if not request.session.get("cart"):
        request.session["cart"] = []
        request.session["total"] = 0
    if category == "regular" or category == "sicilian":
        size = request.POST["size"]
        toppings = []
        if category == "regular":
            for i in range(Regular_Pizza.objects.get(id=dish_id).topping_quantity):
                toppings.append(Topping.objects.get(id=int(request.POST[f"{i}add"])).name)
            product = Regular_Pizza.objects.get(id=dish_id)
        else:
            for i in range(Sicilian_Pizza.objects.get(id=dish_id).topping_quantity):
                toppings.append(Topping.objects.get(id=int(request.POST[f"{i}add"])).name)
            product = Sicilian_Pizza.objects.get(id=dish_id)
        price = getattr(product, size)
        order = {"item": f"{category} {product.name} {size} toppings: {toppings}", "price": price}
        request.session["cart"].append(order)
        request.session["total"] += price
        request.session.modified = True
    elif category == "subs":
        product = Sub.objects.get(id=dish_id)
        size = request.POST["size"]
        adds = []
        price = getattr(product, size)
        for i in range(3):
            add_id = int(request.POST[f"{i}add"])
            if add_id != 1:
                price += 0.5
            adds.append(Extra_Sub.objects.get(id = add_id).name)
        order = {"item": f"{product.name} {size} adds: {adds}", "price": price}
        request.session["cart"].append(order)
        request.session["total"] += price
        request.session.modified = True
    elif category == "salad":
        product = Salad.objects.get(id=dish_id)
        price = product.price
        order = {"item": f"{product.name}", "price": price}
        request.session["cart"].append(order)
        request.session["total"] += price
        request.session.modified = True
    elif category == "pasta":
        product = Pasta.objects.get(id=dish_id)
        price = product.price
        order = {"item": f"{product.name}", "price": price}
        request.session["cart"].append(order)
        request.session["total"] += price
        request.session.modified = True
    elif category == "dinner_platter":
        product = Dinner_Platter.objects.get(id=dish_id)
        size = request.POST["size"]
        price = getattr(product, size)
        order = {"item": f"{product.name} {size}", "price": price}
        request.session["cart"].append(order)
        request.session["total"] += price
        request.session.modified = True



    return render(request, "menu/index.html")

def cart(request):

    order = request.session["cart"]
    total = request.session["total"]
    total = round(total, 2)

    context = {
        "items": order,
        "total": total,
    }

    return render(request, "menu/cart.html", context)