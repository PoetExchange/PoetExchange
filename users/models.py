#####################
# MODEL DEPENDENCIES
#####################
# -------------------
# DEPENDS ON: 'objects' app
# -------------------
# User
# ActivitiesProfile
# -------------------
# DEPENDS ON: 'academics' app
# -------------------
# ActivitiesProfile
# -------------------
# DEPENDS ON: 'excur' app
# -------------------
# ActivitiesProfile

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class SiteUser(models.Model) :
	user				= models.OneToOneField(User)
	area_code	        = models.IntegerField(
                                            max_length=3,
                                            blank=True, null=True,
										)
	phone_prefix		= models.IntegerField(
											max_length=3,
											blank=True, null=True,
										)
	phone_suffix		= models.IntegerField(
											max_length=4,
											blank=True, null=True,
										)
	residence          	= models.ForeignKey('objects.CampusArea',
											blank=True, null=True
										)
	major				= models.ManyToManyField(
                                            'academics.AcademicDepartment',
                                            blank=True, null=True,
										)
	user_photo			= models.ImageField(blank=True, null=True,
											upload_to='/tmp',)
	user_slug			= models.SlugField(editable=False)
	def __unicode__(self) :
		return self.user.username
	def save(self, *args, **kwargs) :
		if not self.id :
			self.user_slug = self.user.username
		super(SiteUser, self).save(*args, **kwargs)
#def create_SiteUser(sender, instance, created, **kwargs) :
#	if created:
#		SiteUser.objects.create(user=instance)
#post_save.connect(create_SiteUser, sender=User)
class RegValidator(models.Model) :
	'''
	This model holds temporary entries for user registration validation number.
	These entries are removed once registration is complete
	'''
	valid_code 			= models.CharField(
											max_length=10,
											unique=True,
										)
	user				= models.CharField(
											max_length=8,
											unique=True,
										)

class ActivitiesProfile(models.Model) :
	user				= models.ForeignKey('SiteUser')
	semester			= models.ForeignKey('objects.Semester')
	classes				= models.ManyToManyField(
											'academics.AcademicClass',
											blank=True, null=True,
										)
	society				= models.ForeignKey(
											'excur.Society',
											blank=True, null=True,
										)
	sports				= models.ManyToManyField(
											'excur.Sport',
											blank=True, null=True,
										)
	extra_curriculars	= models.ManyToManyField(
											'excur.ExtraCurricular',
											blank=True, null=True,
										)
	work_study			= models.BooleanField(
											help_text='Are you eligible for work study?',
										)
	ws_job				= models.ManyToManyField(
											'excur.WorkStudyJob',
											blank=True, null=True,
										)
	unique_key			= models.IntegerField(
											editable=False,
											unique=True,
										)
	def __unicode__(self) :
		value = "%s %s %d" % (self.user.username, self.semester.season, self.semester.year)
		return value
	def save(self, *args, **kwargs) :
		self.unique_key = self.user.pk + self.semester.pk
		super(ActivitiesProfile, self).save(*args, **kwargs)	
