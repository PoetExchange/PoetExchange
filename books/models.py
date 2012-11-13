from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class Book(models.Model) :
	book_title			= models.CharField(max_length=250)
	book_author			= models.CharField(max_length=250)
	book_class			= models.ForeignKey('WhittierClass')
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
	def __unicode__(self) :
		return self.book_title

class WhittierClass(models.Model) :
	class_dept			= models.ForeignKey('Department')
	class_number		= models.IntegerField(max_length=3)
	class_professor		= models.ForeignKey('Professor')
	def __unicode__(self) :
		return self.class_dept.dept_abrv + ' ' + str(self.class_number)
	
class Department(models.Model) :
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
	department			= models.ForeignKey('Department')
	def __unicode__(self) :
		return self.last_name
