from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Order.as_view(), name="order"),
]
