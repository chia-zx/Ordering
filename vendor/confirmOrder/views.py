from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Vendor, Order, OrderItem

# Create your views here.
@login_required
def displayPendingOrder(request):
    vendor = Vendor.objects.get(user=request.user)

    pending_orderid = OrderItem.objects.filter(food_id__vendor_id=vendor, order_id__order_status='Pending').values_list('order_id', flat=True)
    orders = Order.objects.filter(order_id__in=pending_orderid, order_status='Pending')

    context = {
        'year': datetime.now().year,
        'orders': orders
    }
    return render(request, 'displayPendingOrder/displayPendingOrder.html', context)

def displayOrderPendingDetail(request):
    if request.method == 'POST':
        orderid = request.POST.get('order_id')
        orderitems = OrderItem.objects.filter(order_id=orderid)

        context = {
            'year': datetime.now().year,
            'order_id': orderid,
            'orderitems': orderitems,
        }
        return render(request, 'displayPendingOrder/pendingOrderDetail.html', context)

def acceptorder_form(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            context = {
                'year': datetime.now().year,
                'order' : order
            }
            return render(request, 'acceptOrder/acceptOrderForm.html', context)


def acceptorder_confirmation(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            order.order_status = 'Preparing'
            order.save()
            context = {
                'year': datetime.now().year,
                'order' : order,
            }
            
            return render(request, 'acceptOrder/acceptOrderConfirmation.html', context)
        
def rejectorder_form(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            context = {
                'year': datetime.now().year,
                'order' : order
            }
            return render(request, 'rejectOrder/rejectOrderForm.html', context)


def rejectorder_confirmation(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            order.order_status = 'Rejected'
            order.save()

            orderitems = OrderItem.objects.filter(order_id=order_id)

            # Update available quantity for each food in order items
            for orderitem in orderitems:
                food = orderitem.food_id
                food.food_available += orderitem.orderitem_quantity
                food.save()
                
            context = {
                'year': datetime.now().year,
                'order' : order,
                'order_id': order_id
            }
            return render(request, 'rejectOrder/rejectOrderConfirmation.html', context)
