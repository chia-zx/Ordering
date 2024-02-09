from datetime import datetime
from django.shortcuts import redirect, render
from app.models import Food

def deleteitem_form(request):
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        if food_id:
            food = Food.objects.get(pk=food_id)
            context = {
                'year': datetime.now().year,
                'food' : food
            }
            return render(request, 'deleteitem/deleteitemform.html', context)
    return redirect('displayitem')


def deleteitem_confirmation(request):
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        if food_id:
            food = Food.objects.get(pk=food_id)
            food.delete()
            context = {
                'year': datetime.now().year,
                'food' : food,
                'food_id': food_id
            }
            return render(request, 'deleteitem/deleteitemconfirmation.html', context)
