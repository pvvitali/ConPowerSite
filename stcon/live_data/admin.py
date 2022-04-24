from django.contrib import admin

from .models import *

class ListStAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')
    list_dispay_links = ('id', 'number')
    search_fields = ('id', 'number')

class StAdmin(admin.ModelAdmin):
    list_display = ('id', 'u', 'i', 'p1', 'p2', 'time_create')
    list_dispay_links = ('id', 'u', 'i', 'p1', 'p2', 'time_create')
    search_fields = ('id', 'time_create')


class AddressIpAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'ip_address', 'port_address', 'time_create')
    list_dispay_links = ('id', 'number', 'ip_address', 'port_address', 'time_create')
    search_fields = ('id', 'time_create')


admin.site.register(AddressIp, AddressIpAdmin)
admin.site.register(ListSt, ListStAdmin)
admin.site.register(NormelAddressIp)
admin.site.register(NormelListSt)
admin.site.register(St30, StAdmin)
admin.site.register(St31, StAdmin)
admin.site.register(StNormel1)
