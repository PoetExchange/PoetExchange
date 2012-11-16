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
	class_professor		= models.ForeignKey('Professor')
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

class ProfRatingsTable(models.Model) :
	rating_code			= models.CharField(
											max_length=10,
											unique=True,
											blank=True, null=True,
											)
	professor			= models.ForeignKey('Professor')
	user				= models.ForeignKey('users.User')
	rating				= models.IntegerField(
											choices=(
												(-1, '-1'),
												(0, '0'),
												(1, '+1'),
												)
											)
	rating_code			= models.IntegerField(
											unique=True,
											editable=False,
											blank=True, null=True,
											)
	def ratingCodeGenerator(self) :
		'''
		This function creates a unique key for each time a particular user rates a
		particular professor, thereby providing an easy lookup to check if a
		student has already rated a professor.
		'''
		code = "%d%d" % (self.professor, self.user)
		return code
	def save(self) :
		'''
		This function is a custom defined save function which sets the rating code 
		using the function defined above before the entry is put in the database;
		the rating code is only set if the entry is being saved for the first time
		'''
		if not self.id :
			self.rating_code = self.ratingCodeGenerator()
		super(ProfRatingsTable, self).save(*args, **kwargs)
