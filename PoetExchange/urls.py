from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('objects.views',
     url(r'^index/$','index'),
     #url(r'^index/books/$','bookIndex'),
     url(r'^index/books/(?P<book_id>\d+)/$', 'detail'),
)

urlpatterns += patterns('',
     url(r'^index/books/',include('objects.urls')),
     url(r'^admin/', include(admin.site.urls)),
#There are problems with user/views.py, when you uncomment the line below, you won't be able to open admin site. It says there's syntax error..
     #url(r'^profile/$','users.views.initRegistration'),
     #url(r'^signup/$','users.views.signup'),
)
