from django.db import models

class Semester(models.Model) :
	season				= models.CharField(
											max_length=4,
											choices=(

												('FALL', 'Fall'),
												('JNRY', 'January'),
												('SPNG', 'Spring'),
											),
										)
	year				= models.IntegerField(max_length=4)
	is_current			= models.BooleanField()
	def __unicode__(self) :
		sem = "%s %d" % (self.season, self.year)
		return sem

class WeekDay(models.Model) :
	day					= models.CharField(
											max_length=1,
											choices=(
												('M', 'Monday'),
												('T', 'Tuesday'),
												('W', 'Wednesday'),
												('R', 'Thursday'),
												('F', 'Friday'),
												('A', 'Saturday'),
												('U', 'Sunday'),
											),
											unique=True,
										)
	def __unicode__(self):
		return self.day

class CampusArea(models.Model) :
	area				= models.CharField(max_length=50)
	area_type			= models.CharField(
											max_length=2,
											choices=(
												('OD','Outdoor'),
												('CR','Classroom'),
												('FH','Faculty House'),
												('RH','Residence Hall'),
												('MS','Meeting Space'),
												('AB','Administrative Bldg'),
												('OR','Other'),
											),
										)
	def __unicode__(self) :
		return self.area

class CampusRoom(models.Model) :
	room_number			= models.IntegerField(max_length=3)
	area				= models.ForeignKey('CampusArea')
	def __unicode__(self) :
		value = "%s %d" % (self.area, self.room_number)
		return value
