# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class SliderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'designed', 'sort_parameter')
    ordering = ('sort_parameter', )
    
admin.site.register(models.Sign, SliderAdmin)