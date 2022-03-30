from http import HTTPStatus
from django.http import HttpResponse

from django.shortcuts import render


def user_list(request):
    return render(request, 'users/user_list.html')


def user_detail(request, int_id):
    if int_id in (1, ):
        return render(request, 'users/user_detail.html')

    return HttpResponse(status=HTTPStatus.NOT_FOUND)


def signup(request):
    return render(request, 'users/signup.html')


def profile(request):
    return render(request, 'users/profile.html')
