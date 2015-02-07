# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'text',)

admin.site.register(Review, ReviewAdmin)