# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('request_date', 'name', 'phone', 'email',)

admin.site.register(Order, OrderAdmin)