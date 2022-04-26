from datetime import datetime

from django.contrib.auth import get_user_model


def get_birthday_people_email(request):
    birthday_people_email = get_user_model().objects.filter(
        profile__birthday=datetime.now().date()).only('email')
    return {'birthday_people_email': birthday_people_email}
