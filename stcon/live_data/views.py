from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Страница приложения live_data.</h1>")


def station(request, st_id):
    return HttpResponse(f"<h1>Станция номер: {st_id}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')