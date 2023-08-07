from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import order
from .forms import OrderForm

def orders(request):
    myorders = order.objects.all().values()
    template = loader.get_template('orders/customers.html')
    context = {
        'myorders': myorders,
    }
    return HttpResponse(template.render(context,request))
# Create your views here.

def orderForm(request):
    if request.method == 'POST':
        order_num = request.POST['order']
        customer = request.POST['customer']
        truck_num = request.POST['truck']
        delivery_date = request.POST['dates']

        new_order = order(order_number= order_num, delivered_to = customer, truck_number = truck_num, delivery_date = delivery_date)
        new_order.save()


        """ form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or show a success message
    else:
        form = OrderForm() """
    template = loader.get_template('orders/forms.html')
    context = {}
    return HttpResponse(template.render(context,request))