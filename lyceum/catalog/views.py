from django.db.models import Avg, Count
from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Item, ImageModel
from django.views import View
from rating.models import Rating

from rating.forms import RatingUpdateForm


class ItemList(View):
    def get(self, request):
        items = Item.objects.get_name_text_tags__name_category__name()

        context = {"items": items}
        return render(request, "catalog/item_list.html", context=context)


# https://www.youtube.com/watch?v=tajXWvOZyxQ
class ItemDetail(View):
    def get(self, request, int_id):
        item = get_object_or_404(
            Item.objects.get_name_text_tags__name_category__name(), id=int_id
        )
        stars = Rating.objects.filter(item=item, star__in=(1, 2, 3, 4, 5)).aggregate(
            Avg("star"), Count("star")
        )

        images = ImageModel.objects.filter(image_item=int_id).only("catalog_image")
        user_personal = {}
        if request.user.is_authenticated:
            star = (
                Rating.objects.only("star")
                .get_or_create(user=request.user, item=item)[0]
                .star
            )
            form = RatingUpdateForm(
                request.POST or None, initial={"star": star if star else 0}
            )
            user_personal = {"form": form}

        context = {
            "item": item,
            "stars": stars,
            "user_personal": user_personal,
            "images": images,
        }
        return render(request, "catalog/item_detail.html", context=context)

    def post(self, request, int_id):
        item = get_object_or_404(Item.objects.only("id"), id=int_id)
        form = RatingUpdateForm(request.POST or None)
        if form.is_valid() and request.user.is_authenticated:
            rating = item.rating_set.get(user=request.user)
            rating.star = form.cleaned_data["star"]
            rating.save(update_fields=["star"])

        return redirect("catalog:item_detail", int_id=int_id)
