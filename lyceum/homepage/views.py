import random

from django.views import View
from django.shortcuts import render

from catalog.models import Item


class Home(View):
    def get(self, request):
        items = Item.objects.get_name_text_tags__name()
        if items.count() > 3:
            items_id = random.sample(list(items.values_list("id", flat=True)), 3)
            items = items.filter(id__in=items_id)

        context = {"items": items}
        return render(request, "homepage/home.html", context=context)
