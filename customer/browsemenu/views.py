from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Food, Vendor

@login_required
def display_menu(request):
    # v_id = Vendor.objects.get(user=request.user)
    vendor_name = request.GET.get('vendor_name', '')
    foods = Food.objects.all()
    if vendor_name:
        ven = Vendor.objects.get(vendor_name=vendor_name)
        foods = foods.filter(vendor_id = ven.vendor_id)

    vendors = Vendor.objects.all()
    context = {
        'year': datetime.now().year,
        'foods': foods,
        'vendors': vendors
    }
    return render(request, 'browsemenu.html', context)
