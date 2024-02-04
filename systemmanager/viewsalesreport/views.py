from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum;
from app.models import Order, Customer;

@login_required
def viewSalesReport(request):
    num_completed_orders = Order.objects.filter(order_status = 'Completed').count()
    num_cancelled_orders = Order.objects.filter(order_status = 'Cancelled').count()
    customer_spent = Customer.objects.aggregate(total_spent = Sum('customer_spent'))['total_spent'] or 0
    context = {
        'num_completed_orders' : num_completed_orders,
        'num_cancelled_orders' : num_cancelled_orders,
        'customer_spent' : customer_spent,
    }
    return render(request, 'viewsalesreport/viewsalesreport.html', context)