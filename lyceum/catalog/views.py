from django.db.models import Avg, Count
from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Item
from django.views import View
from rating.models import Rating

from rating.forms import RatingUpdateForm


def item_list(request):
    items = Item.objects.get_name_text_tags__name_category__name()

    context = {'items': items}
    return render(request, 'catalog/item_list.html', context=context)


# https://www.youtube.com/watch?v=tajXWvOZyxQ
def item_detail(request, int_id):
    item = get_object_or_404(Item.objects.get_name_text_tags__name_category__name(), id=int_id)

    item_rating = item.rating_set.only('star', 'user')
    rating_count = item_rating.count()
    rating_star_aver = sum(item_rating.values_list('star', flat=True)) / (rating_count or 1)
    rating = {
        'star_aver': rating_star_aver,
        'count': rating_count
    }

    user_personal = {}
    if request.user.is_authenticated:
        star = Rating.objects.get_or_create(user=request.user, item=item)# .values_list('star', flat=True)
        print(star)

        form = RatingUpdateForm(request.POST or None, initial={'star': star})
        if form.is_valid():
            rating = item.rating_set.get(user=request.user)
            rating.star = form.cleaned_data['star']
            rating.save(update_fields=['star'])
            return redirect(f'/catalog/{int_id}')

        eval = Rating.DEGREES_EVALUATION_CHOICES[star - 1][1] if star else '---'
        user_personal = {'form': form, 'eval': eval}

    context = {'item': item, 'rating': rating, 'user_personal': user_personal}
    return render(request, 'catalog/item_detail.html', context=context)


class ItemDetail(View):
    def get(self, request, int_id):
        item = get_object_or_404(Item.objects.get_name_text_tags__name_category__name(), id=int_id)
        stars = Rating.objects.filter(item=item).aggregate(Avg('star'), Count('star'))

        user_personal = {}
        if request.user.is_authenticated:
            star = Rating.objects.get_or_create(user=request.user, item=item)[0].star
            form = RatingUpdateForm(request.POST or None, initial={'star': star if star else 0})
            eval = Rating.DEGREES_EVALUATION_CHOICES[star - 1][1] if star else '---'
            user_personal = {'form': form, 'eval': eval}

        context = {'item': item, 'stars': stars, 'user_personal': user_personal}
        return render(request, 'catalog/item_detail.html', context=context)

    def post(self, request, int_id):
        item = get_object_or_404(Item.objects.only('id'), id=int_id)
        form = RatingUpdateForm(request.POST or None)
        if form.is_valid() and request.user.is_authenticated:
            rating = item.rating_set.get(user=request.user)
            rating.star = form.cleaned_data['star']
            rating.save(update_fields=['star'])

        return redirect('item_detail', int_id=int_id)
