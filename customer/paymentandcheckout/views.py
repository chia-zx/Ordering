from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import Customer, Cart, Order
from app.models import Food
from django.db import transaction
from django.utils import timezone

@login_required
def checkout(request):
    customer = Customer.objects.get(user=request.user)

    if request.method == 'POST':
        with transaction.atomic():
            name = request.POST['name']
            address = request.POST['address']
            phone = request.POST['phone']

            # Update Customer information
            customer.customer_name = name
            customer.customer_address = address
            customer.customer_phone = phone
            customer.save()
            cart = Cart.objects.get(customer_id=customer)
            order = Order.objects.create(
                cart=cart,
                order_date=timezone.now(),
                status='completed'  # Assuming payment was successful
            )

            messages.success(request, 'Your order has been placed successfully!')
            return redirect('order_confirmation', order_id=order.pk)

    return render(request, 'checkout.html', {'customer': customer})


