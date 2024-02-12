from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Customer,Order
from datetime import datetime
from django.db.models import Sum
from decimal import Decimal

@login_required
def customer_total_spent(request):

    # Assuming each User has a corresponding Customer profile
    customer = Customer.objects.get(user=request.user)
        
    # Get the total amount spent from the Customer instance
    total_spent_result = Order.objects.filter(
        customer_id=customer, order_status='Completed'
    ).aggregate(total_spent=Sum('order_totalprice'))
    
    total_spent = total_spent_result['total_spent'] or 0
    total_spent_rounded = round(total_spent, 2)  # Round to 2 decimal places

    # Fetch all completed orders for the customer
    orders = Order.objects.filter(customer_id=customer, order_status='Completed').order_by('-order_date')


    context = {
        'customer_spent': total_spent_rounded,
        'orders': orders,
        'year': datetime.now().year
    }

    return render(request, 'viewtotalspent.html', context)
