# Generated by Django 3.2.12 on 2022-04-27 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_imagemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='image_item',
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='image_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='catalog.item', verbose_name='Вещи'),
        ),
    ]
