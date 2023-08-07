from django import forms
from .models import order

class DateInput(forms.DateInput):
    input_type = 'date'

class OrderForm(forms.ModelForm):
    class Meta:
        model = order
        widgets = {'my_date_field': DateInput}
        #fields = ['order_number', 'delivered_to','truck_number','delivery_date'
        fields = '__all__'
        widgets = {
            'delivery_date': forms.DateInput(
                attrs = { 'type' : 'date', 'placeholder' : 'yyyy-mm-dd(DOB)', 'class': 'form-control'}
            )
        }
