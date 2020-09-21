from django.test import TestCase, Client
from .models import Sicilian_Pizza, Regular_Pizza

class ModelsTestCase(TestCase):

    def setUp(self):
        pizza_r = Regular_Pizza(name = "Cheese", small = 12.7, large = 20, topping_quantity = 0)
        pizza_s = Sicilian_Pizza(name = "Cheese", small = 15.7, large = 23, topping_quantity = 0)
        pizza_2r = Regular_Pizza(name="2 toppings", small=17.7, large=25, topping_quantity=0)
        pizza_2s = Sicilian_Pizza(name="2 toppings", small=19.7, large=28, topping_quantity=0)
        pizza_r.save()
        pizza_s.save()
        pizza_2s.save()
        pizza_2r.save()

    def test_regular(self):
        pizza_r = Regular_Pizza.objects.all()
        self.assertEqual(pizza_r.count(), 2)

    def test_sicilian(self):
        pizza_s = Sicilian_Pizza.objects.all()
        self.assertEqual(pizza_s.count(), 2)

    def test_regular_category_page(self):
        c = Client()
        response = c.get("/category/regular")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["items"].count(), 2)

    def test_sicilian_category_page(self):
        c = Client()
        response = c.get("/category/sicilian")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["items"].count(), 2)

    def test_regular_dish(self):
        pizza_r = Regular_Pizza.objects.get(name = "Cheese")
        pizza_2r = Regular_Pizza.objects.get(name = "2 toppings")

        c = Client()
        response = c.get(f"/category/regular/{pizza_r.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(pizza_r.name, response.context["result"].name)
        self.assertEqual(pizza_r.small, response.context["result"].small)
        self.assertEqual(pizza_r.large, response.context["result"].large)
        self.assertEqual(pizza_r.topping_quantity, response.context["result"].topping_quantity)
        self.assertEqual(pizza_r.image, response.context["result"].image)

        response = c.get(f"/category/regular/{pizza_2r.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(pizza_2r.name, response.context["result"].name)
        self.assertEqual(pizza_2r.small, response.context["result"].small)
        self.assertEqual(pizza_2r.large, response.context["result"].large)
        self.assertEqual(pizza_2r.topping_quantity, response.context["result"].topping_quantity)
        self.assertEqual(pizza_2r.image, response.context["result"].image)

    def test_sicilian_dish(self):
        pizza_s = Sicilian_Pizza.objects.get(name="Cheese")
        pizza_2s = Sicilian_Pizza.objects.get(name="2 toppings")

        c = Client()
        response = c.get(f"/category/sicilian/{pizza_s.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(pizza_s.name, response.context["result"].name)
        self.assertEqual(pizza_s.small, response.context["result"].small)
        self.assertEqual(pizza_s.large, response.context["result"].large)
        self.assertEqual(pizza_s.topping_quantity, response.context["result"].topping_quantity)
        self.assertEqual(pizza_s.image, response.context["result"].image)

        response = c.get(f"/category/sicilian/{pizza_2s.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(pizza_2s.name, response.context["result"].name)
        self.assertEqual(pizza_2s.small, response.context["result"].small)
        self.assertEqual(pizza_2s.large, response.context["result"].large)
        self.assertEqual(pizza_2s.topping_quantity, response.context["result"].topping_quantity)
        self.assertEqual(pizza_2s.image, response.context["result"].image)

    def test_order(self):
        pizza_s = Sicilian_Pizza.objects.get(name="Cheese")
        pizza_2s = Sicilian_Pizza.objects.get(name="2 toppings")
        pizza_r = Regular_Pizza.objects.get(name="Cheese")
        pizza_2r = Regular_Pizza.objects.get(name="2 toppings")
        total = 0

        c = Client()
        response = c.post(f"/category/regular/{pizza_r.id}/order", {"size": "small"})
        self.assertEqual(response.status_code, 200)
        total += pizza_r.small

        response = c.post(f"/category/regular/{pizza_2r.id}/order", {"size": "small"})
        self.assertEqual(response.status_code, 200)
        total += pizza_2r.small

        response = c.post(f"/category/sicilian/{pizza_s.id}/order", {"size": "small"})
        self.assertEqual(response.status_code, 200)
        total += pizza_s.small

        response = c.post(f"/category/sicilian/{pizza_2s.id}/order", {"size": "small"})
        self.assertEqual(response.status_code, 200)
        total += pizza_2s.small

        session = c.session
        self.assertEqual(len(session["cart"]), 4)
        self.assertEqual(session["total"], total)


        response = c.get("/cart", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["items"]), 4)
        self.assertEqual(response.context["total"], total)

        response = c.get("/confirm", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(c.session["total"], 0)
        self.assertEqual(len(c.session["cart"]), 0)








