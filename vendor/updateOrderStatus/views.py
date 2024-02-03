from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Vendor, Order, OrderItem

# Create your views here.
@login_required
def displayPreparingOrder(request):
    vendor = Vendor.objects.get(user=request.user)

    pending_orderid = OrderItem.objects.filter(food_id__vendor_id=vendor, order_id__order_status='Preparing').values_list('order_id', flat=True)
    orders = Order.objects.filter(order_id__in=pending_orderid, order_status='Preparing')

    context = {
        'year': datetime.now().year,
        'orders': orders
    }
    return render(request, 'updateOrderStatus/displayPreparingOrder.html', context)

def completeorder_form(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            context = {
                'year': datetime.now().year,
                'order' : order
            }
            return render(request, 'updateOrderStatus/completeOrderForm.html', context)


def completeorder_confirmation(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        vendor = Vendor.objects.get(user=request.user)
        if order_id:
            order = Order.objects.get(pk=order_id)
            order.order_status = 'Ready'
            order.save()
            vendor.vendor_revenue += order.order_totalprice
            vendor.save()
            context = {
                'year': datetime.now().year,
                'order' : order,
            }
            
            return render(request, 'updateOrderStatus/completeOrderConfirmation.html', context)
        
def cancelorder_form(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            context = {
                'year': datetime.now().year,
                'order' : order
            }
            return render(request, 'updateOrderStatus/cancelOrderForm.html', context)


def cancelorder_confirmation(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            order.order_status = 'Cancelled'
            order.save()
            context = {
                'year': datetime.now().year,
                'order' : order
            }
            return render(request, 'updateOrderStatus/cancelOrderConfirmation.html', context)
