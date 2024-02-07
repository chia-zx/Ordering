from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from app.models import Customer, Vendor, DeliveryPerson, SystemManager

# Create your views here.

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    users = User.objects.filter(is_active=1, is_superuser=0)
    customers = Customer.objects.filter(user__in=users)
    vendors = Vendor.objects.filter(user__in=users)
    deliverypersons = DeliveryPerson.objects.filter(user__in=users)
    managers = SystemManager.objects.filter(user__in=users)

    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
                'customers': customers,
                'vendors': vendors,
                'deliverypersons': deliverypersons,
                'managers': managers,
                'users': users,
            }
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Contact our support for assistance',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Homecook Food Ordering System',
            'message':'This is an food ordering system. There will be 4 main users in this system.',
            'year':datetime.now().year,
        }
    )

@login_required
def menu(request):
    is_vendor = request.user.groups.filter(name='Vendor').exists()
    is_customer = request.user.groups.filter(name='Customer').exists()
    is_delivery_person = request.user.groups.filter(name='DeliveryPerson').exists()
    is_manager = request.user.groups.filter(name='SystemManager').exists()

    context = {
            'title':'Main Menu',
            'is_vendor': is_vendor,
            'is_customer': is_customer,
            'is_delivery_person': is_delivery_person,
            'is_manager': is_manager,
            'year':datetime.now().year,
        }
    context['user'] = request.user

    return render(request,'app/menu.html',context)