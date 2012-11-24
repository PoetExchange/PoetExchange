from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index/', include('objects.urls')),
	url(r'^academics/', include('academics.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^register/', include('users.urls')),
)
