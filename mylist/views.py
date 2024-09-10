from django.shortcuts import render
from .models import ShoppingItem
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def mylist(request):
    if request.method == 'POST':
        print('Method POST')
        print('Received data:', request.POST['itemName'])
        ShoppingItem.objects.create(name = request.POST['itemName'])
    
    elif request.method == 'DELETE':
        print('Method DELETE')
        print('Received data:', request.DELETE['csrfmiddlewaretoken'])

        for item in ShoppingItem.objects.all():
            item.delete()

    else:
        all_items = ShoppingItem.objects.all()
    return render(request, 'shopping_list.html', {"all_items" : all_items})

