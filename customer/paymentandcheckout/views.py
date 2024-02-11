from django.db import transaction
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Cart, CartItem, Order, OrderItem, Payment,Customer
from decimal import Decimal
from datetime import datetime

@login_required
def checkout(request):
    with transaction.atomic():
        customer = request.user.customer  # Adjust according to how you retrieve the Customer instance
        cart = Cart.objects.filter(customer_id=customer).first()

        if not cart:
            return render(request, 'error.html', {'message': 'No cart found.'})

        order = Order.objects.create(
            customer_id=customer,
            order_status='Pending',
            order_totalprice=0
        )

        total_price = Decimal('0.00')
        cart_items = CartItem.objects.filter(cart_id=cart)
        for item in cart_items:
            if item.cartitem_quantity is not None and item.cartitem_totalprice is not None:
                individual_total_price = Decimal(item.cartitem_quantity) * item.cartitem_totalprice
                OrderItem.objects.create(
                    order_id=order,
                    food_id=item.food_id,
                    orderitem_quantity=item.cartitem_quantity,
                    orderitem_totalprice=individual_total_price
                )
                total_price += individual_total_price
            else:
                # Handle the invalid data situation, maybe log it, or raise an error
                raise ValueError(f"Invalid data for CartItem ID {item.cartitem_id}: quantity or total price is None.")

        order.order_totalprice = total_price
        order.save()

        payment, created = Payment.objects.get_or_create(
            order_id=order,
            defaults={'payment_status': 'Pending'}
        )

    context = {
        'order': order,
        'order_items': cart_items,
        'payment': payment,
        'year': datetime.now().year,
    }

    return render(request, 'paymentandcheckout.html', context)
""""
def checkout_confirmation(request):
    customer = request.user.customer  # Retrieve the customer object linked to the request's user
    if request.method == 'POST':
        # Retrieve form data
        customer_name = request.POST.get('customer_name', '').strip()
        customer_address = request.POST.get('customer_address', '').strip()
        customer_phone = request.POST.get('customer_phone', '').strip()

        # Update customer details if provided
        if customer_name:
            customer.customer_name = customer_name
        if customer_address:
            customer.customer_address = customer_address
        if customer_phone:
            customer.customer_phone = customer_phone
        customer.save()

    context = {
        'year': datetime.now().year,

    }
    return render(request, 'paymentandcheckout_confirmation.html', context)

"""
def checkout_confirmation(request):
    customer = request.user.customer  # Retrieve the customer object linked to the request's user
    if request.method == 'POST':
        # Retrieve form data
        customer_name = request.POST.get('customer_name', '').strip()
        customer_address = request.POST.get('customer_address', '').strip()
        customer_phone = request.POST.get('customer_phone', '').strip()

        # Update customer details if provided
        customer.customer_name = customer_name if customer_name else customer.customer_name
        customer.customer_address = customer_address if customer_address else customer.customer_address
        customer.customer_phone = customer_phone if customer_phone else customer.customer_phone
        customer.save()

        # After saving, redirect to a confirmation page, or you could render a template directly
        return render(request, 'paymentandcheckout_confirmation.html', {
            'message': 'Your details have been updated successfully.',
            'year': datetime.now().year,
        })

    # If it's a GET request, render the form with pre-filled customer details
    return render(request, 'paymentandcheckout.html', {
        'customer_name': customer.customer_name,
        'customer_address': customer.customer_address,
        'customer_phone': customer.customer_phone,
        'year': datetime.now().year,
    })