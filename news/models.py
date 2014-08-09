# -*- coding:utf8 -*-
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField('Заголовок', max_length=1024)
    text = models.TextField('Текст')
    date = models.DateField('Дата', blank=True, null=True)
    pass

    class Meta:
        # Сортировка в админке по дате - самый новый впереди
        ordering = ['-date']

    def __unicode__(self):
        return self.title
    
    def 

    def get_absolute_url(self):
        return "/news/%i/" % self.id
    #@models.permalink
    #def get_absolute_url(self):
        #print self.id
        #return ('news.views.news',str(self.id))

class Image(models.Model):
    news = models.ForeignKey(News)
    image = models.ImageField(upload_to='photos/')

