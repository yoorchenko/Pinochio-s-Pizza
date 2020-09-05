from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Regular_Pizza, Topping, Sicilian_Pizza, Sub, Extra_Sub, Pasta, Salad, Dinner_Platter

def index(request):
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

def size_change(request, category, dish_id):
    print(request.POST["size"])
    if category == "sicilian":
        product = Sicilian_Pizza.objects.get(id=dish_id)
    elif category == "regular":
        product = Regular_Pizza.objects.get(id=dish_id)
    response = {"price"}
    return HttpResponse("Yes")