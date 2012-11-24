from django.conf.urls import patterns, include, url

urlpatterns = patterns('objects.views',
	url(r'^$', 'index')
)
