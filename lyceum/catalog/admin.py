from django.contrib import admin

from catalog.models import Item, Tag, Category

admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Category)
