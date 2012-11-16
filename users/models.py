from django.db import models

class User(models.Model) :
	enabled				= models.BooleanField()
	username            = models.CharField(  
											max_length=8,
                                            help_text="Enter poets username",
										)
	area_code	        = models.IntegerField(
                                            max_length=3,
                                            blank=True, null=True,
										)
	phone_prefix		= models.IntegerField(
											max_length=3,
											blank=True, null=True,
										)
	phone_suffix		= models.IntegerField(
											max_length=4,
											blank=True, null=True,
										)
	first_name          = models.CharField(
                                            max_length=75,
										)
	last_name           = models.CharField(
                                            max_length=75,
										)
	residence           = models.CharField(
											max_length=3,
                                            blank=True, null=True,
											choices=(
														('STF', 'Stauffer'),
														('JON', 'Johnson'),
														('BAL', 'Ball'),
														('WRD', 'Wadman'),
														('TRN', 'Turner'),
														('HRS', 'Harris'),
														('WBG', 'Wanberg'),
														('ARB', 'Arbor Ridge'),
														('OFF', 'OffCampus'),
													)
                                            )
	major               = models.ManyToManyField(
                                            'academics.AcademicDepartment',
                                            blank=True, null=True,
										)

class ActivitiesProfile(models.Model) :
	user				= models.ForeignKey('User')
	semester			= models.ForeignKey('objects.Semester')
	classes				= models.ManyToManyField(
											'academics.AcademicClass',
											blank=True, null=True,
										)
	clubs				= models.ManyToManyField(
											'excur.Club',
											blank=True, null=True,
										)
	minority_caucus_groups=models.ManyToManyField(
											'excur.MinorityCaucus',
											blank=True, null=True,
										)
	society				= models.ForeignKey(
											'excur.Society',
											blank=True, null=True,
										)
	sports				= models.ManyToManyField(
											'excur.Sport',
											blank=True, null=True,
										)
	other_extra_curriculars=models.ManyToManyField(
											'excur.ExtraCurricular',
											blank=True, null=True,
										)
	work_study			= models.BooleanField(
											help_text='Are you eligible for work study?',
										)
	ws_job				= models.ManyToManyField(
											'excur.WorkStudyJob',
											blank=True, null=True,
										)
