from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from app.models import Order, OrderItem, Vendor

@login_required
def viewAllVendor(request):
    sort_by = request.GET.get('vendor')

    if sort_by == 'ID':
        vendors = Vendor.objects.all().order_by('vendor_id')
    elif sort_by == 'Name':
        vendors = Vendor.objects.all().order_by('vendor_name')
    elif sort_by == 'Revenue':
        vendors = Vendor.objects.all().order_by('vendor_revenue')
    else:
        vendors = Vendor.objects.all()
        # ? display all (name, phone, address, revenue)

    for vendor in vendors:
        complete_orderid = OrderItem.objects.filter(
                                food_id__vendor_id=vendor.vendor_id, 
                                order_id__order_status='Completed').values_list('order_id', flat=True)
        orders = Order.objects.filter(order_id__in=complete_orderid, order_status='Completed')

        total_revenue = orders.aggregate(Sum('order_totalprice'))['order_totalprice__sum'] or 0
        total_revenue = "{:.2f}".format(total_revenue)

        vendor.vendor_revenue = total_revenue
        vendor.save()

    context = {
        'vendors' : vendors,
        'sort_by' : sort_by,
    }
    return render(request, 'viewvendor/viewvendor.html', context)