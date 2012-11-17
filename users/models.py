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

class User(models.Model) :
	enabled				= models.BooleanField()
	username            = models.CharField(  
											max_length=8,
                                            help_text="Enter poets username",
										)
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
	first_name          = models.CharField(
                                            max_length=75,
										)
	last_name           = models.CharField(
                                            max_length=75,
										)
	residence           = models.ForeignKey('objects.CampusArea')
	major               = models.ManyToManyField(
                                            'academics.AcademicDepartment',
                                            blank=True, null=True,
										)
	def __unicode__(self) :
		return self.username

class ActivitiesProfile(models.Model) :
	user				= models.ForeignKey('User')
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
	def __unicode__(self) :
		value = "%s %s %d" % (self.user.username, self.semester.season, self.semester.year)
		return value

	
