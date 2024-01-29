from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
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
            'message':'Dr. Yeoh.',
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
            'title':'ABC System',
            'message':'This application processes ...',
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