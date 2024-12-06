from django.urls import path
from . import views

app_name = 'func'

urlpatterns = [
    path("", views.menu, name="order"),
]