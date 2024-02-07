from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import Food
from app.forms import Itemform
from django.db import transaction

# Create your views here.

@login_required
def updateitemform(request):
    food_id = request.POST.get('food_id')
    food = Food.objects.get(pk=food_id)
    form = Itemform(instance=food)
    context = {
        'title':'Update Item Form',
        'year': datetime.now().year,
        'food': food,
        'form': form
    }

    context['user'] = request.user

    return render(request,'updateitem/updateitemform.html',context)

@transaction.atomic
def updateitemconfirmation(request):
    if request.method == 'POST':
        with transaction.atomic():
            food_id = request.POST.get('food_id')
            food = Food.objects.get(pk=food_id)
            form = Itemform(request.POST, instance=food)
            if form.is_valid():
                form.instance.vendor_id = food.vendor_id
                form.save()
                context = {
                    'food' : food
                }
                
                return render(request,'updateitem/updateitemconfirmation.html',context)
        