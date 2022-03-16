from http import HTTPStatus
from django.http import HttpResponse


def user_list(request):
    return HttpResponse('Список пользователей')


def user_detail(request, int_id):
    if int_id in (1, ):
        return HttpResponse('Информация о пользователе')

    return HttpResponse(status=HTTPStatus.NOT_FOUND)


def signup(request):
    return HttpResponse('Регистрация')


def profile(request):
    return HttpResponse('Мой профиль')
