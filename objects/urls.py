from django.conf.urls import patterns, include, url

urlpatterns = patterns('objects.views',
	url(r'^$','bookIndex'),
	url(r'^books/(?P<book_id>\d+)/$', 'detail'),
)
