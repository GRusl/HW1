from django.shortcuts import render, get_object_or_404

from catalog.models import Item


def item_list(request):
    items = Item.objects.get_for_write()

    return render(request, 'catalog/item_list.html', context={'items': items})


def item_detail(request, int_id):
    item = get_object_or_404(Item, id=int_id)

    return render(request, 'catalog/item_detail.html', context={'item': item})
