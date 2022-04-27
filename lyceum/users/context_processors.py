from django.contrib.auth import get_user_model
from django.utils import timezone


def get_birthday_people_email(request):
    birthday_people_email = (
        get_user_model()
        .objects.filter(profile__birthday=timezone.now())
        .only("email")
    )
    return {"birthday_people_email": birthday_people_email}
