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
    return render(request, 'displayPreparingOrder/displayPreparingOrder.html', context)

def displayOrderPreparingDetail(request):
    if request.method == 'POST':
        orderid = request.POST.get('order_id')
        orderitems = OrderItem.objects.filter(order_id=orderid)

        context = {
            'year': datetime.now().year,
            'order_id': orderid,
            'orderitems': orderitems,
        }
        return render(request, 'displayPreparingOrder/orderPreparingDetail.html', context)

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
                'order' : order,
            }
            return render(request, 'updateOrderStatus/cancelOrderForm.html', context)


def cancelorder_confirmation(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            order.order_status = 'Cancelled'
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
            return render(request, 'updateOrderStatus/cancelOrderConfirmation.html', context)
