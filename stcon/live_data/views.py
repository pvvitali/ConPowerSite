from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

def index(request):
    station_list = ListSt.objects.all()
    station_normel_list = NormelListSt.objects.all()
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'Home'
    }
    return render(request, 'live_data/index.html', context=context)

def logs(request):
    station_list = ListSt.objects.all()
    station_normel_list = NormelListSt.objects.all()
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'Logs'
    }
    return render(request, 'live_data/logs.html', context=context)


def control(request):
    station_list = ListSt.objects.all()
    station_normel_list = NormelListSt.objects.all()
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'Control'
    }
    return render(request, 'live_data/control.html', context=context)


def contacts(request):
    station_list = ListSt.objects.all()
    station_normel_list = NormelListSt.objects.all()
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'Contacts'
    }
    return render(request, 'live_data/contacts.html', context=context)


def help_site(request):
    station_list = ListSt.objects.all()
    station_normel_list = NormelListSt.objects.all()
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'Help'
    }
    return render(request, 'live_data/help_site.html', context=context)


def about(request):
    station_list = ListSt.objects.all()
    station_normel_list = NormelListSt.objects.all()
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'About'
    }
    return render(request, 'live_data/about.html', context=context)



def station(request, st_id):
    station_list = ListSt.objects.all()
    station_normel_list = NormelListSt.objects.all()
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'Data',
        'st_id': str(st_id)
    }
    return render(request, 'live_data/station.html', context=context)


def station_normel(request, st_id):
    station_list = ListSt.objects.all()
    station_normel_list = NormelListSt.objects.all()
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'title': 'Data',
        'st_id': str(st_id)
    }
    return render(request, 'live_data/station_normel.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')