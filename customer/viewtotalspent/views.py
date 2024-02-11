from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Customer,Order
from datetime import datetime

@login_required
def customer_total_spent(request):

    # Assuming each User has a corresponding Customer profile
    customer = Customer.objects.get(user=request.user)
        
    # Get the total amount spent from the Customer instance
    customer_spent = customer.customer_spent

    # Fetch all completed orders for the customer
    orders = Order.objects.filter(customer_id=customer, order_status='Completed').order_by('-order_date')


    context = {
        'customer_spent': customer_spent,
        'orders': orders,
        'year': datetime.now().year
    }

    return render(request, 'viewtotalspent.html', context)
