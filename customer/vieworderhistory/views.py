# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.models import Order

@login_required
def view_order_history(request):
    # Fetch all orders for the logged-in user, excluding those still being processed
    completed_orders = Order.objects.filter(customer=request.user, status__in=['completed', 'shipped', 'delivered']).order_by('-order_date')

    # Fetch orders that are still being processed
    processing_orders = Order.objects.filter(customer=request.user, status='processing').order_by('-order_date')

    return render(request, 'customer/order_history.html', {
        'completed_orders': completed_orders,
        'processing_orders': processing_orders,
    })
