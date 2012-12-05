from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns( 'users.views',
	url(r'^register/$', 'initRegistration'),
	url(r'^register/(?P<user_slug>[a-z0-9]{2,8})/$', 'mainRegistration'),
)
