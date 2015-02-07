# -*- coding: utf-8 -*-
from django.db import models
from pytils import dt, translit

class Review(models.Model):
    name  = models.CharField(u'название', max_length=255)
    url  = models.CharField(u'адрес сайта', blank=True, max_length=255)
    text = models.TextField(u'текст')
                    
    class Meta:
        verbose_name = u'отзыв'
        verbose_name_plural = u'отзывы'
        ordering = ['-name']

    def __unicode__(self):
        return self.name
