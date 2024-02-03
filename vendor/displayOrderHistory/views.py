from datetime import datetime
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Order

# Create your views here.
@login_required 
def displayOrderHistory(request):
    if request.method == 'GET':
        order_status = request.GET.get('order_status')

        # Filter the queryset based on the sorting parameter
        queryset = Order.objects.all()

        if order_status:
            queryset = queryset.filter(order_status=order_status)

        context = {
            'year': datetime.now().year,
            'orders': queryset
        }
        return render(request, 'displayOrderHistory/displayOrderHistory.html', context)
    else:
        context = {
            'year': datetime.now().year,
        }
        return render(request, 'displayOrderHistory/displayOrderHistory.html', context)