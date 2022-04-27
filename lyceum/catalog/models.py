from django.db import models
from django.db.models import Prefetch
from sorl.thumbnail import get_thumbnail
from tinymce.models import HTMLField
from catalog.validators import MinNumWordsValidator, OccurrenceWordsValidator
from django.utils.safestring import mark_safe
from core.models import PublicationBaseModel, SlugBaseModel


class ItemManager(models.Manager):
    def get_name_text_tags__name(self):
        return (
            self.get_queryset()
            .filter(is_published=True, category__is_published=True)
            .only("name", "text")
            .prefetch_related(
                Prefetch("tags", queryset=Tag.objects.get_published().only("name"))
            )
        )

    def get_name_text_tags__name_category__name(self):
        return (
            self.get_queryset()
            .filter(is_published=True, category__is_published=True)
            .select_related("category")
            .only("name", "text", "category__name")
            .prefetch_related(
                Prefetch("tags", queryset=Tag.objects.get_published().only("name"))
            )
        )


class Tag(PublicationBaseModel, SlugBaseModel):
    name = models.CharField(
        "Название",
        max_length=150,
        default="",
        help_text="Максимальная длина - 150 символов",
    )

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class Category(PublicationBaseModel, SlugBaseModel):
    name = models.CharField(
        "Название",
        max_length=150,
        default="",
        help_text="Максимальная длина - 150 символов",
    )
    weight = models.PositiveSmallIntegerField("Вес", default=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("weight",)

    def __str__(self):
        return self.name


class Item(PublicationBaseModel):
    name = models.CharField(
        "Название", max_length=150, help_text="Максимальная длина - 150 символов"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="Категория"
    )
    tags = models.ManyToManyField(Tag, verbose_name="Тэги")
    text = HTMLField(
        "Описание",
        validators=(
            MinNumWordsValidator(2),
            OccurrenceWordsValidator(("превосходно", "роскошно")),
        ),
        help_text='Минимум два слова. Обязательно содержится слово "превосходно" или "роскошно"',
    )
    upload = models.ImageField(upload_to="uploads/", null=True)

    def get_image_x1280(self):
        return get_thumbnail(self.upload, "400", quality=51)

    def get_image_400x300(self):
        return get_thumbnail(self.upload, "100x100", quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(f'<img src="{self.upload.url}" width="50">')
        return "нет изоражения"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("category__weight",)

    def __str__(self):
        return self.name

    objects = ItemManager()


class ImageModel(models.Model):
    catalog_image = models.ImageField(upload_to="uploads/", null=True)
    image_item = models.ForeignKey(Item, on_delete=models.PROTECT, verbose_name="Вещи", default=None)

    def get_image_400x300(self):
        return get_thumbnail(self.catalog_image, "100x100", quality=51)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
