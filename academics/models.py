#####################
# MODEL DEPENDENCIES
#####################
# ------------------
# DEPENDS ON: 'objects' app
# ------------------
# AcademicClassProfile
# ------------------
# DEPENDS ON: 'users' app
# -----------------
# Book


from django.db import models
from django.core.validators import MaxLengthValidator
from django.template.defaultfilters import slugify

class Book(models.Model) :
	book_seller			= models.ForeignKey('users.SiteUser')
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
	entry_date			= models.DateTimeField(auto_now=True,)
	user_class_key		= models.IntegerField(editable=False,)
	book_slug			= models.SlugField(editable=False,)
	def __unicode__(self) :
		return self.book_title
	def save(self,*args,**kwargs) :
		if not self.id :
			self.book_slug = self.pk
		self.user_class_key = self.book_seller.pk + self.book_class.pk
		super(Book, self).save(*args, **kwargs)

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
	unique_key			= models.IntegerField(
										editable=False,
										unique=True,
									)
	ac_slug				= models.SlugField(editable=False)
	def __unicode__(self) :
		return self.class_dept.dept_abrv + ' ' + str(self.class_number)
	def save(self, *args, **kwargs) :
		if not self.id :
			unslugged = "%s %d" % (self.class_dept.dept_abrv, self.class_number)
			self.ac_slug = slugify(unslugged)
		self.unique_key = self.class_dept.pk + self.class_number
		super(AcademicClass, self).save(*args, **kwargs)
	
class AcademicDepartment(models.Model) :
	dept_name			= models.CharField(
											max_length=250,
											unique=True,
										)
	dept_abrv			= models.CharField(
											max_length=4,
											unique=True,
										)
	dept_slug			= models.SlugField(editable=False)
	def __unicode__(self) :
		return self.dept_abrv
	def save(self, *args, **kwargs) :
		if not self.id :
			dept_slug = slugify(self.dept_abrv)
		super(AcademicDepartment, self).save(*args, **kwargs)

class Professor(models.Model) :
	first_name			= models.CharField(
											max_length=50,
											blank=True, null=True,
											)
	last_name			= models.CharField(max_length=80)
	department			= models.ForeignKey('AcademicDepartment')
	unique_key			= models.CharField(
											max_length=100,
											editable=False,
											unique=True,
										)
	def __unicode__(self) :
		return self.last_name
	def save(self, *args, **kwargs) :
		self.unique_key = self.last_name + self.department.dept_abrv
		super(Professor, self).save(*args, **kwargs)

class AcademicClassProfile(models.Model) :
	ac_class			= models.ForeignKey('AcademicClass')
	semester			= models.ForeignKey('objects.Semester')
	meeting_days		= models.ManyToManyField(
											'objects.WeekDay',
											blank=True, null=True,
										)
	meeting_time		= models.TimeField(blank=True, null=True)
	meeting_room		= models.ForeignKey(
											'objects.CampusRoom',
											blank=True, null=True,
										)
	unique_key			= models.IntegerField(
											editable=False,
											unique=True,
										)
	def __unicode__(self) :
		value = "%s %s" % (self.ac_class, self.semester)
		return value
	def save(self, *args, **kwargs) :
			self.unique_key = self.ac_class.pk + self.semester.pk
			super(AcademicClassProfile, self).save(*args, **kwargs)
		

