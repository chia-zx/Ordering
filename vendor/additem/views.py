from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import Food, Vendor
from app.forms import Itemform

# Create your views here.

@login_required
def additemform(request):
    form = Itemform()
    context = {
        'title':'Add Item Form',
        'year': datetime.now().year,
        'form': form
    }
    context['user'] = request.user

    return render(request,'additem/additemform.html',context)

def additemconfirmation(request):
    if request.method == 'POST':
        form = Itemform(request.POST)
        if form.is_valid():
            vendor = Vendor.objects.get(user=request.user)
            form.instance.vendor_id = vendor
            form.save()
            food_id = form.instance.pk
            food = Food.objects.get(pk=food_id)
            context = {
                'food' : food
            }
            return render(request,'additem/additemconfirmation.html',context)
