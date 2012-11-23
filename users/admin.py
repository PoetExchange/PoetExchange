from users.models import SiteUser, ActivitiesProfile, RegValidator
#Import some more classes, if you've modified in the models.py
from django.contrib import admin

class userList(admin.ModelAdmin):
	#You can add more attributes in the list_display if you've modified some of them.
	list_display = ('user','area_code','phone_prefix','phone_suffix','residence')

admin.site.register(SiteUser,userList)
admin.site.register(ActivitiesProfile)
#I'm not sure if RegValidator is supposed to be showed up
admin.site.register(RegValidator)
