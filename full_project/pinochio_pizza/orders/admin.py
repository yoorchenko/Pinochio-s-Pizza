from django.contrib import admin
from .models import User, Order, Item

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ("items",)

admin.site.register(User)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item)
