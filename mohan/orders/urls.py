from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('orders/', views.orders, name = 'orders'),
    path('forms/', views.orderForm, name = 'orderForm')
]