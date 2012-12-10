from users.models import *
#Import some more classes, if you've modified in the models.py
from django.contrib import admin

class userList(admin.ModelAdmin):
	#You can add more attributes in the list_display if you've modified some of them.
	list_display = ('user','area_code','phone_prefix','phone_suffix','residence','user_photo')

admin.site.register(SiteUser,userList)
admin.site.register(ActivitiesProfile)
# RegValidator should not be registered; this class works as an underpinning to the registration framework
#admin.site.register(RegValidator)
