from django.db import transaction
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Cart, CartItem, Order, OrderItem, Payment,Customer
from decimal import Decimal
from datetime import datetime
from app.forms import CustomerForm

@login_required
def checkout(request):
    form = CustomerForm()
    with transaction.atomic():
        customer = request.user.customer  # Adjust according to how you retrieve the Customer instance
        cart = Cart.objects.filter(customer_id=customer).first()
        if not cart:
            message = 'Please add items to your cart before checking out'
            context={
                'message': message,
                'year': datetime.now().year,
            }
            return render(request,'addtocart.html',context)

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
            defaults={'payment_status': 'Success'}
        )

    context = {
        'order': order,
        'order_items': cart_items,
        'payment': payment,
        'year': datetime.now().year,
        'form': form
    }

    context['user'] = request.user

    return render(request, 'paymentandcheckout.html', context)

@login_required
def checkout_confirmation(request):
    customer = request.user.customer
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            cart = Cart.objects.filter(customer_id=customer).first()
            if cart:
                CartItem.objects.filter(cart_id=cart).delete()
                cart.delete()
            payment = Payment.objects.filter(order_id__customer_id=customer).order_by('-payment_date').first()
            context = {
                'payment': payment,
                'form': form,
                'year': datetime.now().year
         }
            return render(request, 'paymentandcheckout_confirmation.html', context)
