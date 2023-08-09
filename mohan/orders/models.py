from django.db import models
from django import forms
from datetime import date

class DateInput(forms.DateInput):
    input_type = 'date'

# Create your models here.
class order(models.Model):
    order_number = models.AutoField( primary_key=True)
    invoice_number = models.CharField(max_length=30,null=True)
    order_date = models.DateField(default=date(2023,8,7))
    customer_name = models.CharField(max_length=30, null=True)
    #payment = models.SmallIntegerField(null=True)
    quantity = models.IntegerField(null=True)
    deposit_amount = models.FloatField(null=True)
    price_per_item = models.FloatField(null=True)
    total_price = models.FloatField(null=True)
    desc = models.CharField(max_length=50,null=True)
    #delivery_date = models.DateField(widget = DateInput)

class DeliveryNote(models.Model):
    delivery = models.ForeignKey(order, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=20)  # 'Shoes', 'Plastics', 'Chemicals'
    truck_number = models.SmallIntegerField()

#Shoes
class ShoeOrder(models.Model):
    orders = models.ForeignKey(order, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=20)  # 'Shoes', 'Plastics', 'Chemicals'
    quantity = models.IntegerField()
    size = models.SmallIntegerField()
#EVA
""" class EvaOrder(models.Model):
    orders = models.ForeignKey(order, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=20)  # 'Shoes', 'Plastics', 'Chemicals'
    bags = models.IntegerField()
    kilos = models.IntegerField()
#PVC
class PvcOrder(models.Model):
    orders = models.ForeignKey(order, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=20)  # 'Shoes', 'Plastics', 'Chemicals'
    bags = models.IntegerField()
    kilos = models.IntegerField() """

