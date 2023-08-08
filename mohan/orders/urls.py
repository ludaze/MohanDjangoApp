from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('orders/', views.orders, name = 'orders'),
    path('forms/', views.orderForm, name = 'orderForm'),
    path('shoes/', views.shoe_orders, name = 'shoe_orders'),
    path('eva/', views.eva_orders, name = 'eva_orders'),
    path('pvc/', views.pvc_orders, name = 'pvc_orders'),
]