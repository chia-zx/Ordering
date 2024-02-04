from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import DeliveryPerson;

@login_required
def viewAllDeliveryperson(request):
    sort_by = request.GET.get('deliveryperson')

    if sort_by == 'ID':
        deliverypersons = DeliveryPerson.objects.all().order_by('deliveryperson_id').values()
    elif sort_by == 'Name':
        deliverypersons = DeliveryPerson.objects.all().order_by('deliveryperson_name').values()
    else:
        deliverypersons = DeliveryPerson.objects.all().values()
        # ? display all (name, phone, address)

    context = {
        'deliverypersons' : deliverypersons,
        'sort_by' : sort_by,
    }
    return render(request, 'viewdeliveryperson/viewdeliveryperson.html', context)