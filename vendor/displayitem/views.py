from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Food, Vendor

@login_required
def display_all_items(request):
    v_id = Vendor.objects.get(user=request.user)
    foods = Food.objects.filter(vendor_id = v_id)
    context = {
        'year': datetime.now().year,
        'foods': foods
    }
    return render(request, 'displayitem/displayitem.html', context)
