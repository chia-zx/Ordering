from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import DeliveryPerson, Vendor, Order

# Create your views here.
@login_required
def displayReadyOrder(request):

    orders = Order.objects.filter(order_status="Ready")
    context = {
        'year': datetime.now().year,
        'orders': orders
    }
    return render(request, 'selectorders.html', context)

def acceptdelivery_confirmation(request):
    deliveryperson = DeliveryPerson.objects.get(user=request.user)
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            order.order_status = 'Delivering'
            order.deliveryperson_id = deliveryperson
            order.save()
            context = {
                'year': datetime.now().year,
                'order' : order,
            }
            
            return render(request, 'acceptdeliveryconfirmation.html', context)