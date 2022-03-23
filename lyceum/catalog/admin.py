from django.contrib import admin

from catalog.models import Item, Tag, Category


class ItemAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Tag)
admin.site.register(Category)
