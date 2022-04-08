import random

from django.shortcuts import render

from catalog.models import Item, Tag


def home(request):
    items = Item.objects.get_for_write()
    if items.count() > 3:
        items_id = random.sample(list(items.values_list('id', flat=True)), 3)
        items = Item.objects.filter(id__in=items_id)

    context = {'items': items}
    return render(request, 'homepage/home.html', context=context)
