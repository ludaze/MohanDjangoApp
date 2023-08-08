from django.db import models
from django import forms
from datetime import date

class DateInput(forms.DateInput):
    input_type = 'date'

# Create your models here.
class order(models.Model):
    order_number = models.SmallIntegerField()
    delivered_to = models.CharField(max_length=30)
    truck_number = models.SmallIntegerField()
    delivery_date = models.DateField(default=date(2023,8,7))
    #delivery_date = models.DateField(widget = DateInput)


