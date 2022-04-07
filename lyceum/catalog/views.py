from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404

from catalog.models import Item, Tag


def item_list(request):
    items = Item.objects.get_published().only('name', 'text').prefetch_related(
        Prefetch('tags', queryset=Tag.objects.get_published().only('name')))

    context = {'items': items}
    return render(request, 'catalog/item_list.html', context=context)


def item_detail(request, int_id):
    item = get_object_or_404(Item, id=int_id)

    context = {'item': item}
    return render(request, 'catalog/item_detail.html', context=context)
