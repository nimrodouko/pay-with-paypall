from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from .models import Order
from django.shortcuts import get_object_or_404

def homepage(request):
    return render('home.html')




def process_payment(request):
    
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,id=order_id)
    host =request.get_host()


    paypal_dict ={
        'business':settings.PAYPAL_RECIEVER_EMAIL,
        'amount':'%2f'% order.total_cost().quantize(Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',

    }
   






# Create your views here.
