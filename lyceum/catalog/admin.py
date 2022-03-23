from django.contrib import admin

from catalog.models import Item, Tag, Category


class ItemAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags', )

    list_display = ('name', 'is_published')
    list_display_links = ('name', )
    list_editable = ('is_published', )


admin.site.register(Item, ItemAdmin)
admin.site.register(Tag)
admin.site.register(Category)
