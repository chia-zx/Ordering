from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Vendor, Order, OrderItem
from django.contrib import messages

# Create your views here.
@login_required
def displayReadyOrder(request):

    orders = Order.objects.filter(order_status="Ready")
    context = {
        'year': datetime.now().year,
        'orders': orders
    }
    return render(request, 'selectorders.html', context)
