#####################
# MODEL DEPENDENCIES
#####################
# ------------------
# DEPENDS ON: 'objects' app
# ------------------
# AcademicClassProfile


from django.db import models
from django.core.validators import MaxLengthValidator

class Book(models.Model) :
	book_title			= models.CharField(max_length=250)
	book_author			= models.CharField(max_length=250)
	book_class			= models.ForeignKey('AcademicClass')
	book_price			= models.IntegerField(max_length=3)
	book_condition		= models.CharField(
											max_length=2,
											choices=(
												('BN', 'Brand New'),
												('EX', 'Excellent'),
												('GD', 'Good'),
												('FR', 'Fair'),
												('WT', 'Weathered'),
												('BD', 'Bad'),
												),
										)
	additional_comments	= models.TextField(
											validators=[MaxLengthValidator(500)],
											blank=True, null=True,
											)
	entry_date			= models.DateTimeField(auto_now=True)
	def __unicode__(self) :
		return self.book_title

class AcademicClass(models.Model) :
	class_dept			= models.ForeignKey('AcademicDepartment')
	class_number		= models.IntegerField(max_length=3)
	class_name			= models.CharField(
										max_length=100,
										blank=True, null=True,
									)
	class_professor		= models.ForeignKey(
										'Professor',
										blank=True, null=True,
									)
	last_updated		= models.DateTimeField(auto_now=True)
	def __unicode__(self) :
		return self.class_dept.dept_abrv + ' ' + str(self.class_number)
	
class AcademicDepartment(models.Model) :
	dept_name			= models.CharField(max_length=250)
	dept_abrv			= models.CharField(max_length=4)
	def __unicode__(self) :
		return self.dept_abrv

class Professor(models.Model) :
	first_name			= models.CharField(
											max_length=50,
											blank=True, null=True,
											)
	last_name			= models.CharField(max_length=80)
	department			= models.ForeignKey('AcademicDepartment')
	def __unicode__(self) :
		return self.last_name

class AcademicClassProfile(models.Model) :
	ac_class			= models.ForeignKey('AcademicClass')
	semester			= models.ForeignKey('objects.Semester')
	meeting_days		= models.ManyToManyField(
											'objects.WeekDay',
											blank=True, null=True
										)
	meeting_time		= models.TimeField(blank=True, null=True)
	meeting_room		= models.ForeignKey(
											'objects.CampusRoom',
											blank=True, null=True,
										)
	def __unicode__(self) :
		value = "%s %s" % (self.ac_class, self.semester)
		return value

