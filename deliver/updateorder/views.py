from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import DeliveryPerson, Order, OrderItem

# Create your views here.


@login_required
def update_status(request):
    delivery_person = DeliveryPerson.objects.get(user=request.user)
    readydeliveryids = Order.objects.filter(deliveryperson_id=delivery_person, order_status='Ready').values_list('order_id', flat=True)
    orders = Order.objects.filter(order_id__in=readydeliveryids)
    context = {
        'year': datetime.now().year,
        'orders': orders,
        'no_orders': not orders.exists()  # This will be True if there are no orders
    }
    return render(request, 'updateorder/completeconfirmation.html', context)
    
def ViewReadyOrder(request):

    delivery_person = DeliveryPerson.objects.get(user=request.user)
    readydeliveryids = Order.objects.filter(delivery_person=delivery_person, order_status='Ready').values_list('id', flat=True)
    orders = Order.objects.filter(id__in=readydeliveryids)

    context = {
        'year': datetime.now().year,
        'orders': orders
    }
    return render(request, 'viewreadyorder/viewreadyorder.html', context)


def ViewReadyOrderDetail(request):
    if request.method == 'POST':
        orderid = request.POST.get('order_id')
        orderitems = OrderItem.objects.filter(order_id=orderid)

        context = {
            'year': datetime.now().year,
            'order_id': orderid,
            'orderitems': orderitems,
        }
        return render(request, 'viewreadyorder/readyorderdetail.html', context)

def complete_form(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            context = {
                'year': datetime.now().year,
                'order': order
            }
            return render(request, 'updateorder/completeform.html', context)

def complete_confirmation(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            order.order_status = 'Delivered' 
            order.save()
            context = {
                'year': datetime.now().year,
                'order': order,
            }
            return render(request, 'updateorder/completeconfirmation.html', context)

def cancel_form(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            context = {
                'year': datetime.now().year,
                'order': order,
            }
            return render(request, 'updateorder/cancelform.html', context)

def cancel_confirmation(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(pk=order_id)
            order.order_status = 'Cancelled'
            order.save()

            context = {
                'year': datetime.now().year,
                'order': order,
                'order_id': order_id
            }
            return render(request, 'updateorder/cancelconfirmation.html', context)