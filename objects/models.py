from django.db import models
from django.template.defaultfilters import slugify

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
	unique_key			= models.CharField(
											editable=False,
											unique=True,
											max_length=8,
										)
	semester_slug		= models.SlugField(editable=False)
	def __unicode__(self) :
		sem = "%s %d" % (self.season, self.year)
		return sem
	def save(self, *args, **kwargs) :
		self.unique_key = "%s%d" % (self.season, self.year)
		if not self.id :
			self.semester_slug = slugify(self.unique_key)
		super(Semester, self).save(*args, **kwargs)

class WeekDay(models.Model) :
	day					= models.CharField(
											max_length=3,
											choices=(
												('MON', 'Monday'),
												('TUE', 'Tuesday'),
												('WED', 'Wednesday'),
												('THR', 'Thursday'),
												('FRI', 'Friday'),
												('SAT', 'Saturday'),
												('SUN', 'Sunday'),
											),
											unique=True,
										)
	def __unicode__(self):
		return self.day

class CampusArea(models.Model) :
	area				= models.CharField(
											max_length=50,
											unique=True,
										)
	area_type			= models.CharField(
											max_length=2,
											choices=(
												('OD','Outdoor'),
												('AC','Academic Building'),
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
	unique_key			= models.IntegerField(
											editable=False,
											unique=True,
										)
	def __unicode__(self) :
		value = "%s %d" % (self.area, self.room_number)
		return value
	def save(self, *args, **kwargs) :
		self.unique_key = self.area.pk + self.room_number
		super(CampusRoom, self).save(*args, **kwargs)
