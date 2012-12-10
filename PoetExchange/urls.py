from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^login/$', 'users.views.loginRequest'),
	url(r'^logout/$', 'users.views.logoutRequest'),
    url(r'^$', include('objects.urls')),
	url(r'^academics/', include('academics.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^user/', include('users.urls')),
)
