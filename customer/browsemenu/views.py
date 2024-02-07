# customer/views.py

from django.shortcuts import render
from app.models import Food  # Import your Food and Vendor models correctly
from app.models import Vendor

def browse_menu(request):
    # Check if a vendor_id is provided for filtering
    vendor_id = request.GET.get('vendor_id', None)
    vendors = Vendor.objects.all()  # Get all vendors to display in the dropdown
    
    if vendor_id:
        # If a vendor_id is provided, filter food items by the vendor
        food_items = Food.objects.filter(vendor_id=vendor_id)
    else:
        # If no vendor_id is provided, display all food items
        food_items = Food.objects.all()
    
    # Pass the food items and vendors to the template
    context = {
        'food_items': food_items,
        'vendors': vendors,  # Add the vendors to the context
    }
    return render(request, 'browsemenu/browsemenu.html', context)
