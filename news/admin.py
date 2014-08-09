# -*- coding:utf8 -*-
from django.contrib import admin
from news.models import News, Image


# Настраиваем столбцы для отображения в админке
class InlineImage(admin.TabularInline):
    model = Image

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'date')
    inlines = [InlineImage,]

admin.site.register(News, NewsAdmin)
