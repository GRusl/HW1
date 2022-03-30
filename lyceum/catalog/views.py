from http import HTTPStatus
from django.http import HttpResponse

from django.shortcuts import render


def item_list(request):
    return render(request, 'catalog/item_list.html')


def item_detail(request, int_id):
    if int_id in (1, 2):
        return render(request, 'catalog/item_detail.html')

    return HttpResponse(status=HTTPStatus.NOT_FOUND)
