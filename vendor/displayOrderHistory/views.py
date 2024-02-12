from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Order, OrderItem, Vendor

# Create your views here.
@login_required 
def displayOrderHistory(request):
    vendor = Vendor.objects.get(user=request.user)

    filter_status = ['Rejected', 'Completed', 'Cancelled']
    ordersFilterByStatus = Order.objects.filter(order_status__in=filter_status)

    if request.method == 'GET':
        selected_order_status = request.GET.get('order_status')
        if selected_order_status:
            ordersFilterByStatus = Order.objects.filter(order_status=selected_order_status)

    orders_id = OrderItem.objects.filter(orderitem_id__in=ordersFilterByStatus, food_id__vendor_id=vendor).values_list('order_id', flat=True)
    orders = Order.objects.filter(order_id__in=orders_id)

    context = {
        'year': datetime.now().year,
        'orders': orders,
    }
    return render(request, 'displayOrderHistory/displayOrderHistory.html', context)

    
def displayOrderHistoryDetail(request):
    if request.method == 'POST':
        orderid = request.POST.get('order_id')
        orderitems = OrderItem.objects.filter(order_id=orderid)
        
        context = {
            'year': datetime.now().year,
            'order_id': orderid,
            'orderitems': orderitems,
        }
        return render(request, 'displayOrderHistory/orderHistoryDetail.html', context)