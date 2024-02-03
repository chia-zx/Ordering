from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Vendor, Order, OrderItem
from django.contrib import messages

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
    return render(request, 'confirmOrder/displayPendingOrder.html', context)

def acceptorder_form(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            context = {
                'year': datetime.now().year,
                'order' : order
            }
            return render(request, 'confirmOrder/acceptOrderForm.html', context)


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
            
            return render(request, 'confirmOrder/acceptOrderConfirmation.html', context)
        
def rejectorder_form(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            context = {
                'year': datetime.now().year,
                'order' : order
            }
            return render(request, 'confirmOrder/rejectOrderForm.html', context)


def rejectorder_confirmation(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            order.order_status = 'Rejected'
            order.save()
            context = {
                'year': datetime.now().year,
                'order' : order
            }
            return render(request, 'confirmOrder/rejectOrderConfirmation.html', context)
