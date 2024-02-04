from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Vendor;

@login_required
def viewAllVendor(request):
    sort_by = request.GET.get('vendor')

    if sort_by == 'ID':
        vendors = Vendor.objects.all().order_by('vendor_id').values()
    elif sort_by == 'Name':
        vendors = Vendor.objects.all().order_by('vendor_name').values()
    elif sort_by == 'Revenue':
        vendors = Vendor.objects.all().order_by('vendor_revenue').values()
    else:
        vendors = Vendor.objects.all().values()
        # ? display all (name, phone, address, revenue)

    context = {
        'vendors' : vendors,
        'sort_by' : sort_by,
    }
    return render(request, 'viewvendor/viewvendor.html', context)