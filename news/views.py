#-*- coding=utf8 -*-
'''
Created on 16.06.2012

@author: jskonst
'''
#import glob
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#import settings
from news.models import News

def news(request, news_id):
    p = get_object_or_404(News,pk=news_id)
    return render_to_response('news.html', {'item': p}, RequestContext(request))

