from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
#Calendar
import calendar
import datetime


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



def station(request, st_id, day_s=0, month_s=0, year_s=0, day_r=0, month_r=0, year_r=0):
    station_list = ListSt.objects.all()
    station_normel_list = NormelListSt.objects.all()
    #Список моделей
    st = {30:St30, 31:St31, 32:St32, 33:St33}
    station_data = st[st_id].objects.order_by('-id')[:10]
    #Календарь -------------------------------------------------------------------------
    now = datetime.datetime.now()
    if day_s == 0 or month_s == 0 or year_s == 0 :
        day_s=now.day; month_s=now.month; year_s=now.year
    month_days_s = calendar.monthcalendar(year_s, month_s)
    month_s_str = calendar.month_name[month_s]

    if day_r == 0 or month_r == 0 or year_r == 0 :
        day_r=now.day; month_r=now.month; year_r=now.year
    month_days_r = calendar.monthcalendar(year_r, month_r)
    month_r_str = calendar.month_name[month_r]
    

    #-----------------------------------------------------------------------------------
    context = {
        'station_list': station_list,
        'station_normel_list': station_normel_list,
        'station_data': station_data,
        'title': 'Data',
        'st_id': str(st_id),
        'month_days_s': month_days_s,
        'day_s': day_s,
        'month_s': month_s,
        'year_s': year_s,
        'month_s_str': month_s_str,
        'month_days_r': month_days_r,
        'day_r': day_r,
        'month_r': month_r,
        'year_r': year_r,
        'month_r_str': month_r_str,
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



# ----------------------------------------------------------------------------------------
# XMLHttpRequest()

def getdata(request):
    if request.method == 'GET':
        return JsonResponse({"key":"post"})    #save=False => any type, else only dict
    elif request.method == 'POST':
        try:
            day_left = request.POST["day_left"]
            month_left  = request.POST["month_left"]
            year_left  = request.POST["year_left"]
            day_right = request.POST["day_right"]
            month_right  = request.POST["month_right"]
            year_right  = request.POST["year_right"]
        except:
            day_left = 0
            month_left  = 0
            year_left  = 0
            day_right = 0
            month_right  = 0
            year_right  = 0
        #print(month_left, year_left)
        return JsonResponse({"day_left": day_left, "month_left": month_left, "year_left": year_left,
            "day_right": day_right, "month_right": month_right, "year_right": year_right})




def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')