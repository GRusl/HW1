from http import HTTPStatus
from django.http import HttpResponse


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(request, int_id):
    if int_id in (1, 2):
        return HttpResponse('Подробно элемент')

    return HttpResponse(status=HTTPStatus.NOT_FOUND)
