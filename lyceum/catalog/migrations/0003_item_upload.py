# Generated by Django 3.2.12 on 2022-04-27 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_item_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="upload",
            field=models.ImageField(null=True, upload_to="uploads/"),
        ),
    ]
