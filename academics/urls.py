from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('academics.views',
#		url(r'^books/$', 'bookIndex'),
#		url(r'^books/(?P<book_id>\d+)/$', 'bookDetail'),
		url(r'^(?P<slug>[A-Z]{3,4})/$', 'deptDetail')
)
