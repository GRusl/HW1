from django.contrib import admin

from catalog.models import Item, Tag, Category, ImageModel


class ItemAdmin(admin.ModelAdmin):
    filter_horizontal = ("tags",)

    list_display = ("name", "is_published", "image_tmb")
    list_display_links = ("name",)
    list_editable = ("is_published",)


admin.site.register(Item, ItemAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(ImageModel)
