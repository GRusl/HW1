# Generated by Django 3.2.12 on 2022-03-23 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_auto_20220323_2034'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField(choices=[(1, 'Ненависть'), (2, 'Неприязнь'), (3, 'Нейтрально'), (4, 'Обожание'), (5, 'Любовь')], null=True, verbose_name='Оценка')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.item', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('user', 'item'), name='unique appversion'),
        ),
    ]
