from django.shortcuts import render, get_object_or_404
from app.models import Food, Cart, CartItem, Customer
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def add_to_cart(request):
    # Ensure that this view only works with POST method to handle form submission
    if request.method == "POST":
        food_id = request.POST.get('food_id')
        food_price = Food.objects.get(pk=food_id).food_price
        user = request.user
        customer, _ = Customer.objects.get_or_create(user=user)

        # Retrieve the Food instance
        food = get_object_or_404(Food, pk=food_id)

        # Retrieve or create a Cart for the logged-in customer
        cart, created = Cart.objects.get_or_create(customer_id=customer, defaults={'customer_id': customer})

        # Check if the CartItem already exists
        cart_item, created = CartItem.objects.get_or_create(cart_id=cart, food_id=food, defaults={'cartitem_quantity': 1},cartitem_totalprice = food_price)
        if not created:
            # If the item already exists, update the quantity instead
            cart_item.cartitem_quantity += 1
            cart_item.save()

        
        context = {
            'food': food,
            'year': datetime.now().year
            }

        return render(request,'addtocart.html', context) 


