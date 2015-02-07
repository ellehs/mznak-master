# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class TextBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'id')
    search_fields = ('title', 'content')

admin.site.register(models.TextBlock, TextBlockAdmin)