from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "prepare"

urlpatterns = [
    path('', views.Ordering.as_view(), name="order"),
]
