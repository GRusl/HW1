import random

from django.db.models import Prefetch
from django.shortcuts import render

from catalog.models import Item, Tag


def home(request):
    items = Item.objects.get_published().only('name', 'text').prefetch_related(
        Prefetch('tags', queryset=Tag.objects.get_published().only('name')))
    if len(items) > 3:
        items_id = random.sample(list(items.values_list('id', flat=True)), 3)
        items = Item.objects.filter(id__in=items_id)

    context = {'items': items}
    return render(request, 'homepage/home.html', context=context)
