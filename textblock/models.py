# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

class TextBlock(models.Model):
    title = models.CharField(max_length=512, verbose_name=u'описание')
    content = RichTextField(blank=True, verbose_name=u'контент')
        
    class Meta:
        verbose_name = u'текстовый блок'
        verbose_name_plural = u'текстовые блоки'
        ordering=['id']
        
    def __unicode__(self):
        return self.title
    
    @staticmethod 
    def get_by_id(id_):
        return TextBlock.objects.get(id=id_).content