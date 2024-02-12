from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from app.models import Customer, Order;

@login_required
def viewAllCustomer(request):
    sort_by = request.GET.get('customer')

    if sort_by == 'ID':
        customers = Customer.objects.all().order_by('customer_id')
    elif sort_by == 'Name':
        customers = Customer.objects.all().order_by('customer_name')
    elif sort_by == 'Spent':
        customers = Customer.objects.all().order_by('customer_spent')
    else:
        customers = Customer.objects.all()
        # ? display all (name, phone, address, spent)

    for customer in customers:
        orders = Order.objects.filter(customer_id=customer.customer_id, order_status='Completed')

        total_spent = orders.aggregate(Sum('order_totalprice'))['order_totalprice__sum'] or 0
        total_spent = "{:.2f}".format(total_spent)

        customer.customer_spent = total_spent
        customer.save()

    context = {
        'customers' : customers,
        'sort_by' : sort_by,
    }
    return render(request, 'viewcustomer/viewcustomer.html', context)