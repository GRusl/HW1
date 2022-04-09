from django.shortcuts import render, get_object_or_404

from catalog.models import Item


def item_list(request):
    items = Item.objects.get_name_text_tags__name_category__name()

    context = {'items': items}
    return render(request, 'catalog/item_list.html', context=context)


def item_detail(request, int_id):
    item = get_object_or_404(Item.objects.get_name_text_tags__name_category__name(), id=int_id)

    context = {'item': item}
    return render(request, 'catalog/item_detail.html', context=context)
