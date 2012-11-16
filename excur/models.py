from django.db import models
from django.core.validators import MaxLengthValidator

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

class ExtraCurricular(models.Model) :
	group_name			= models.CharField(max_length=30)
	group_description	= models.TextField(
									validators=[MaxLengthValidator(500)],
									blank=True, null=True,
								)
	group_type			= models.CharField(
									max_length=2,
									choices=(
										('CB','Club'),
										('MC','Minority Caucus'),
										('SG','Student Government'),
										('SM','Student Media'),
										('HS','Honors Society'),
										('OR','Other'),
									),
								)
	is_active			= models.BooleanField(default=True)
	def __unicode__(self) :
		return self.group_name

class Society(models.Model) :
	group_name			= models.CharField(max_length=12)
	group_description	= models.TextField(
									validators=[MaxLengthValidator(500)],
									blank=True, null=True,
								)
	is_active			= models.BooleanField(default=True)
	def __unicode__(self) :
		return self.group_name

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
	def __unicode__(self) :
		return self.sport_name

class ExtraCurricularProfile(models.Model) :
	group				= models.ForeignKey('ExtraCurricular')
	semester			= models.ForeignKey('objects.Semester')
	meeting_days		= models.ManyToManyField(
									'objects.WeekDay',
									blank=True, null=True,
								)
	meeting_time		= models.TimeField(blank=True, null=True)
	meeting_area		= models.ForeignKey(
									'objects.CampusArea',
									blank=True, null=True,
								)
	meeting_room		= models.ForeignKey(
									'objects.CampusRoom',
									blank=True, null=True,
								)
#	officers
	def __unicode__(self) :
		value = "%s %s" % (self.group, self.semester)
		return value


#class SportProfile :
#class SocietyProfile :
#	society				= models.ForeignKey('Society')
#	semester			= models.ForeignKey('objects.Semester')
#	officers	
