from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from app.models import Food, Cart, CartItem
from app.models import Customer  # Replace with your user model if different

@login_required
def add_to_cart(request, food_id):
    food_item = get_object_or_404(Food, pk=food_id)
    customer = get_object_or_404(Customer, user=request.user)  # Adjust based on your Customer model relationship to User

    if food_item.food_available > 0:
        # Get or create a cart for the customer
        cart, created = Cart.objects.get_or_create(customer_id=customer, defaults={'cart_date': timezone.now()})
        
        # Get or create a cart item for this food item
        cart_item, created = CartItem.objects.get_or_create(
            cart_id=cart,
            food_id=food_item,
            defaults={'cartitem_quantity': 1}
        )
        if not created:
            # If the cart item already exists, increase the quantity
            cart_item.cartitem_quantity += 1
            cart_item.save()

        messages.success(request, "Item added to cart successfully!")
    else:
        messages.error(request, "This item is not available.")

    return redirect('addtocart')  # Replace 'menu_page' with the name of your menu page URL

# Make sure to create the corresponding URL pattern in your urls.py:
# path('add_to_cart/<int:food_id>/', views.add_to_cart, name='add_to_cart')
