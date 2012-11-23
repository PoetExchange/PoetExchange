from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^index/$','objects.views.index'),
     #url(r'^index/books/$','objects.views.bookIndex'),
     url(r'^index/books/(?P<book_id>\d+)/$', 'objects.views.detail'),
     url(r'^index/books/',include('objects.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^register/', include('users.urls')),
)
