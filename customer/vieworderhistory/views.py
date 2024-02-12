from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Order
from datetime import datetime

@login_required
def customer_order_history(request):

    orders = Order.objects.filter(customer_id__user=request.user, order_status='Completed').order_by('-order_date')

    context = {
        'orders': orders,
        'year': datetime.now().year
    }

    return render(request, 'vieworderhistory.html', context)
