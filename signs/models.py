# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

class Sign(models.Model):
    image = models.ImageField(upload_to= 'uploads/signs', max_length=256, verbose_name=u'картинка')
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'порядок сортировки', help_text=u'№ слайдера: 1й, 2й .. 5й')
    designed = models.BooleanField(u'разработано нами', blank=True, default=False, help_text=u'Пометьте галочкой, если нужно отображать в блоке с разработанными')
    
    def save(self, *args, **kwargs):
        super(Sign, self).save(*args, **kwargs)
        if not self.sort_parameter:
            self.sort_parameter=self.id
            self.save()
        
    
    class Meta:
        verbose_name = u'знак'
        verbose_name_plural = u'знаки'
        ordering = ['sort_parameter']
        
    
    def __unicode__(self):
        return str(self.image)