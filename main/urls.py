# -*- coding=utf8 -*-
#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns, include, url
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    # Подключаем урлы приложения конференция
    #url(r'^accounts/', include('conference.urls')),
    #url(r'^', include('conference.urls')),
    #url(r'^', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home'),  # Основная страница с информацией
    url(r'^about/$', 'main.views.about'),  # Основная страница с информацией
    url(r'^abiturient/$', 'main.views.abiturient'),  # Основная страница с информацией
    url(r'^students/$', 'main.views.students'),  # Основная страница с информацией
    url(r'^tutors/$', 'main.views.tutors'),  # Основная страница с информацией
    url(r'^news/(?P<news_id>\d+)/', 'news.views.news'),  # Основная страница с информацией
    #чтобы правильно отображать статику на сервере
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
