from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Customer;

@login_required
def viewAllCustomer(request):
    sort_by = request.GET.get('customer')

    if sort_by == 'ID':
        customers = Customer.objects.all().order_by('customer_id').values()
    elif sort_by == 'Name':
        customers = Customer.objects.all().order_by('customer_name').values()
    elif sort_by == 'Spent':
        customers = Customer.objects.all().order_by('customer_spent').values()
    else:
        customers = Customer.objects.all().values()
        # ? display all (name, phone, address, spent)

    context = {
        'customers' : customers,
        'sort_by' : sort_by,
    }
    return render(request, 'viewcustomer/viewcustomer.html', context)