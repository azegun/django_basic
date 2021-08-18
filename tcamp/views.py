from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("장고 논산입니다 환영합니다.")