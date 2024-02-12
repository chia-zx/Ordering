from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Order
from datetime import datetime
# Create your views here.
@login_required
def viewhistory(request):
    
    orders = Order.objects.filter(deliveryperson_id__user=request.user, order_status__in=['Completed', 'Cancelled']).order_by('-order_date')

    context = {
        'orders': orders,
        'year': datetime.now().year,
    }
    return render(request, 'viewhistory.html', context)
