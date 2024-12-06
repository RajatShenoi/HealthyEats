from django.contrib import admin

from func.models import Cart, CartEntry, Item

# Register your models here.
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartEntry)