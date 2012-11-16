from django.db import models

class Semester(models.Model) :
	season				= models.CharField(
											max_length=4,
											choices=(
												('FALL', 'Fall'),
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

