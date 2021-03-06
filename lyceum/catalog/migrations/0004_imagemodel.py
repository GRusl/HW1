# Generated by Django 3.2.12 on 2022-04-27 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_item_upload"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("catalog_image", models.ImageField(null=True, upload_to="uploads/")),
                (
                    "image_item",
                    models.ManyToManyField(to="catalog.Item", verbose_name="Вещи"),
                ),
            ],
            options={
                "verbose_name": "Изображение",
                "verbose_name_plural": "Изображения",
            },
        ),
    ]
