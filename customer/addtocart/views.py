from django.shortcuts import render, get_object_or_404
from app.models import Food, Cart, CartItem, Customer
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def add_to_cart(request):
    if request.method == "POST":
        food_id = request.POST.get('food_id')
        food_price = Food.objects.get(pk=food_id).food_price
        food = get_object_or_404(Food, pk=food_id)

        if food.food_available <= 0:
            message = 'sorry, Food is not available'
            context={
                'message': message,
                'year': datetime.now().year,
            }
            return render(request,'addtocart.html',context)
           
        user = request.user
        customer, _ = Customer.objects.get_or_create(user=user)


        food = get_object_or_404(Food, pk=food_id)

        food.food_available -= 1
        food.save()


        cart, created = Cart.objects.get_or_create(customer_id=customer, defaults={'customer_id': customer})


        cart_item, created = CartItem.objects.get_or_create(cart_id=cart, food_id=food, defaults={'cartitem_quantity': 1},cartitem_totalprice = food_price)
        if not created:

            cart_item.cartitem_quantity += 1
            cart_item.save()

        
        context = {
            'food': food,
            'year': datetime.now().year
            }

        return render(request,'addtocart.html', context) 


