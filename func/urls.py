from django.urls import path
from . import views

app_name = 'func'

urlpatterns = [
    path("", views.menu, name="order"),
    path("add/<int:item_id>", views.addToCart, name="add"),
    path("remove/<int:cartEntryId>", views.removeFromCart, name="remove"),
    path("cart", views.cart, name="cart"),
]