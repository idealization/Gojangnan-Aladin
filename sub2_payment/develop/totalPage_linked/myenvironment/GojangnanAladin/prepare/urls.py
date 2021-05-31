from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "prepare"

urlpatterns = [
    path('', views.Order.as_view(), name="order"),
    path('result/', views.add_order, name='add_order')
]
