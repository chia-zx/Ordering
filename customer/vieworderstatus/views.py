from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Order
from datetime import datetime

@login_required
def customer_order_status(request):
    orders = Order.objects.exclude(order_status='Completed').filter(customer_id__user=request.user).order_by('-order_date')

    context = {
        'orders': orders,
        'year': datetime.now().year
    }

    return render(request, 'vieworderstatus.html', context)
