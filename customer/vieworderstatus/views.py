from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Customer, Order

@login_required
def view_order_status(request):
    customer = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(customer=customer).order_by('-order_date')
    
    return render(request, 'order_status.html', {'orders': orders})
