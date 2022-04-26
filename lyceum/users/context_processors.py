import django.utils.datetime_safe
from django.contrib.auth import get_user_model


def get_birthday_people_name(request):
    birthday_people_name = get_user_model().objects.filter(
        profile__birthday=django.utils.datetime_safe.date).only('name')
    return {'birthday_people_name': birthday_people_name}
