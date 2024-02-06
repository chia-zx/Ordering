# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.models import Customer

@login_required
def view_total_spent(request):
    customer = Customer.objects.get(user=request.user)
    total_spent = customer.customer_spent

    # Check if the customer has any orders
    if total_spent > 0:
        message = f"Total amount spent: ${total_spent}"
    else:
        message = "There was no past order and the total spent will be zero."

    return render(request, 'customer/total_spent.html', {'message': message})
