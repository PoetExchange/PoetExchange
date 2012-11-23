from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns( 'users.views',
	url(r'^$', 'initRegistration'),
)
