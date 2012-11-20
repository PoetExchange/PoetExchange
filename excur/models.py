######################
# MODEL DEPENDENCIES
######################
# --------------------
# DEPENDS ON: 'academics' app
# --------------------
# WorkStudyJob
# --------------------
# DEPENDS ON: 'users' app
# --------------------
# ExtrCurOfficer
# TeamCapt
# --------------------
# DEPENDS ON: 'objects' app
# --------------------
# ExtraCurricularProfile
# SocietyProfile
# SportProfile
# ExtrCurOfficer
from django.db import models
from django.core.validators import MaxLengthValidator
from django.template.defaultfilters import slugify

class AdministrativeDepartment(models.Model) :
	dept_name			= models.CharField(
										max_length=250,
										unique=True
									)
	dept_description	= models.TextField(
										validators=[MaxLengthValidator(500)],
										blank=True, null=True,
									)
	dept_slug			= models.SlugField(editable=False)
	def __unicode__(self) :
		return self.dept_name
	def save(self, *args, **kwargs) :
		if not self.id :
			self.dept_slug = slugify(self.dept_name)
		super(AdministrativeDept, self).save(*args, **kwargs)

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
	unique_key			= models.CharField(
									editable=False,
									max_length=54,
									unique=True,
								)
	job_slug			= models.SlugField(editable=False)	
	def __unicode__(self) :
		job = "%s%s %s" % (self.academic_dept, self.administrative_dept, self.job_title)
		return job
	def save(self, *args, **kwargs) :
		if not self.id :
			unslugged = self.academic_dept + self.administrative_dept + ' ' + self.job_title
			self.job_slug = slugify(unslugged)
		self.unique_key= "%d%d%s" % (self.academic_dept.pk, self.administrative_dept.pk, self.job_title)
		super(WorkStudyJob, self).save(*args, **kwargs)

class ExtraCurricular(models.Model) :
	group_name			= models.CharField(
									max_length=30,
									unique=True,
								)
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
	group_slug			= models.SlugField(editable=False)
	def __unicode__(self) :
		return self.group_name
	def save(self, *args, **kwargs) :
		if not self.id :
			self.group_slug = slugify(group_name)
		super(ExtraCurricular, self).save(*args, **kwargs)

class Society(models.Model) :
	group_name			= models.CharField(
											max_length=12,
											unique=True,
										)
	group_description	= models.TextField(
									validators=[MaxLengthValidator(500)],
									blank=True, null=True,
								)
	is_active			= models.BooleanField(default=True)
	group_slug			= models.SlugField(editable=False)
	def __unicode__(self) :
		return self.group_name
	def save(self, *args, **kwargs) :
		if not self.id :
			self.group_slug = slugify(group_name)
		super(Society, self).save(*args, **kwargs)

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
	sport_slug			= models.SlugField(editable=False)
	def __unicode__(self) :
		return self.sport_name
	def save(self, *args, **kwargs) :
		if not self.id :
			self.sport_slug = slugify(sport_name)
		super(Sport, self).save(*args, **kwargs)

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
	unique_key			= models.IntegerField(
									max_length=8,
									editable=False,
									unique=True,
								)
	def __unicode__(self) :
		value = "%s %s" % (self.group, self.semester)
		return value
	def save(self, *args, **kwargs) :
		self.unique_key = int("%d%d" % (self.group.pk, self.semester.pk))
		super(ExtraCurricularProfile, self).save(*args, **kwargs)

class SocietyProfile(models.Model) :
	group				= models.ForeignKey('Society')
	semester			= models.ForeignKey('objects.Semester')
	unique_key			= models.IntegerField(
									max_length=8,
									editable=False,
									unique=True,
								)
	def __unicode__(self) :
		value = "%s %s" % (self.group, self.semester)
		return value
	def save(self, *args, **kwargs) :
		self.unique_key = int("%d%d" % (self.group.pk, self.semester.pk))
		super(SocietyProfile, self).save(*args, **kwargs)

class SportProfile(models.Model) :
	sport				= models.ForeignKey('Sport')
	semester			= models.ForeignKey('objects.Semester')
	unique_key			= models.IntegerField(
									max_length=8,
									editable=False,
									unique=True,
								)
	def __unicode__(self) :
		value = "%s %s" % (self.group, self.semester)
		return value
	def save(self, *args, **kwargs) :
		self.unique_key = int("%d%d" % (self.group.pk, self.semester.pk))
		super(SportProfile, self).save(*args, **kwargs)

class ExtrCurOfficer(models.Model) :
	position_name		= models.CharField(max_length=30)
	position_semester	= models.ForeignKey('objects.Semester')
	user				= models.ForeignKey('users.SiteUser')
	group_type			= models.CharField(
									max_length=1,
									choices=(
										('SO', 'Society'),
										('CB', 'Club'),
										('MC','Minority Caucus'),
										('SG','Student Government'),
										('SM','Student Media'),
										('HS','Honors Society'),
										('OR','Other'),
									)
								)
	ex_cur_group		= models.ForeignKey(
										'ExtraCurricular',
										blank=True, null=True
									)
	society_group		= models.ForeignKey(
										'Society',
										blank=True, null=True,
									)
	slug_group			= models.CharField(
										max_length=30,
										editable=False,
									)
	def __unicode__(self) :
		value = "%s%s %s" % (self.ex_cur_profile, self.society_profile, self.position_names)
		return value
	def save(self,*args, **kwargs) :
		self.slug_group = slugify(self.position_name)
		super(ExtrCurOfficer, self).save(*args, **kwargs)

class TeamCapt(models.Model) :
	user				= models.ForeignKey('users.SiteUser')
	sport				= models.ForeignKey('Sport')
	year				= models.IntegerField(max_length=4)
	unique_key			= models.IntegerField(
										editable=False,
										unique=True,
									)
	def __unicode__(self) :
		value = "%s %s %s %d" % (self.user.first_name, self.user.last_name, self.sport, self.year)
		return value
	def save(self, *args, **kwargs) :
		self.unique_key = self.user.pk + self.sport.pk + self.year.pk
		super(TeamCapt, self).save(*args, **kwargs)
