from django.shortcuts import render, get_object_or_404

from catalog.models import Item

from rating.forms import RatingUpdateForm


def item_list(request):
    items = Item.objects.get_name_text_tags__name_category__name()

    context = {'items': items}
    return render(request, 'catalog/item_list.html', context=context)


def item_detail(request, int_id):
    item = get_object_or_404(Item.objects.get_name_text_tags__name_category__name(), id=int_id)

    item_rating = item.rating_set.only('star')
    rating_count = item_rating.count()
    rating_star_aver = sum(item_rating.values_list('id', flat=True)) / rating_count
    rating = {
        'star_aver': rating_star_aver,
        'count': rating_count
    }

    context = {'item': item, 'rating': rating}
    return render(request, 'catalog/item_detail.html', context=context)
