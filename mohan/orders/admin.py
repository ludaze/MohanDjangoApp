from django.contrib import admin
from .models import order
# Register your models here.
""" class OrderAdmin(admin.ModelAdmin):
    list_display= ('order_number', 'customer_name', 'order_Date')
    
  
admin.site.register(order, OrderAdmin) """

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number',)