from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class AdministrativeDepartment(models.Model) :
	dept_name			= models.CharField(max_length=250)
	dept_description	= models.TextField(
											validators=[MaxLengthValidator(500)],
											blank=True, null=True,
										)
	def __unicode__(self) :
		return self.dept_name

class WorkStudyJob(models.Model) :
	dept_type 			= models.CharField(
									max_length=2,
									choices=(
										('AC', 'Academic'),
										('AD', 'Administrative'),
									),
							)
	academic_dept 		= models.ForeignKey(
									'academics.AcademicDepartment',
									blank=True, null=True,
								)
	administrative_dept = models.ForeignKey(
									'AdministrativeDepartment',
									blank=True, null=True,
								)
	job_title			= models.CharField(
									max_length=50,
								)
	def __unicode__(self) :
		job = "%s%s %s" % (self.academic_dept, self.administrative_dept, self.job_title)
		return job

class Club(models.Model) :
	club_name			= models.CharField(max_length=30)
	club_description	= models.TextField(
									validators=[MaxLengthValidator(500)],
									blank=True, null=True,
								)
	is_active			= models.BooleanField(default=True)

class MinorityCaucus(models.Model) :
	group_name			= models.CharField(max_length=30)
	group_description	= models.TextField(
									validators=[MaxLengthValidator(500)],
									blank=True, null=True,
								)
	is_active			= models.BooleanField(default=True)

class Society(models.Model) :
	group_name			= models.CharField(max_length=12)
	group_description	= models.TextField(
									validators=[MaxLengthValidator(500)],
									blank=True, null=True,
								)
	is_active			= models.BooleanField(default=True)

class Sport(models.Model) :
	sport_name			= models.CharField(
									max_length=15,
									unique=True,
								)
	sport_season		= models.CharField(
									max_length=4,
									choices=(
										('FALL', 'Fall'),
										('WNTR', 'Winter'),
										('SPNG', 'Spring'),
									)
								)

class ExtraCurricular(models.Model) :
	activity_name		= models.CharField(
									max_length=30,
								)
	activity_description=models.TextField(validators=[MaxLengthValidator(500)])
	
