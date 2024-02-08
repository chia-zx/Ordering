import calendar
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from app.models import Vendor, Order, OrderItem

# Create your views here.
@login_required
def displayRevenue(request):
    if request.method == 'GET':
        vendor = Vendor.objects.get(user=request.user)

        getYear = request.GET.get('year')
        getMonth = request.GET.get('month')
        years_range = range(2023, datetime.now().year + 1)
        months_range = range(1, 13)
        months_range = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

        complete_orderid = OrderItem.objects.filter(
                            food_id__vendor_id=vendor, 
                            order_id__order_status='Completed').values_list('order_id', flat=True)
        
        # Convert getMonth to integer if it exists
        if getMonth:
            intMonth = months_range.index(getMonth) + 1 

        # Filter orders based on selected month and year
        if getYear and not getMonth:
            orders = Order.objects.filter(
                order_id__in=complete_orderid,
                order_status='Completed',
                order_date__year=getYear
            )
        elif getYear and getMonth:
            orders = Order.objects.filter(
                order_id__in=complete_orderid,
                order_status='Completed',
                order_date__year=getYear,
                order_date__month=intMonth
            )
        else:
            orders = Order.objects.filter(order_id__in=complete_orderid, order_status='Completed')

        total_revenue = orders.aggregate(Sum('order_totalprice'))['order_totalprice__sum'] or 0
        total_revenue = "{:.2f}".format(total_revenue)

        context = {
            'year': datetime.now().year,
            'vendor': vendor,
            'revenue': total_revenue,
            'orders': orders,
            'years_range': years_range,
            'months_range': months_range,
            'getYear': getYear,
            'getMonth': getMonth,
        }
        return render(request, 'displayRevenue/displayRevenue.html', context)
    else:
        context = {
            'year': datetime.now().year,
        }
        return render(request, 'displayRevenue/displayRevenue.html', context)
    
