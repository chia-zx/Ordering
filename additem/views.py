from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import Item

# Create your views here.

@login_required
def additemform(request):
    context = {
        'title':'Add Item Form',
        'year': datetime.now().year,
    }
    context['user'] = request.user

    return render(request,'additem/additemform.html',context)

def additemconfirmation(request):
 
    newitem_id = request.POST['item_id']
    newitem_name= request.POST['item_name']
    newitem_description = request.POST['item_description']

    newitem = Item(item_id = newitem_id,
                   item_name = newitem_name, 
                   item_description = newitem_description)

    newitem.save()
    context = {
        'item_id': newitem_id,
        'item_name' : newitem_name,
        'item_description' : newitem_description,
    }
    
    return render(request,'additem/additemconfirmation.html',context)
