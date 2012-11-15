from django.db import models

class User(models.Model) :
	enabled				= models.BooleanField()
	username            = models.EmailField(
											max_length=254,
                                            help_text="Enter valid poets email address",
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
                                            		'objects.AcademicDepartment',
                                            		blank=True, null=True,
                                            		)
'''
**The following attributes reference models which have not yet been created**

    work_study          = models.BooleanField(help_text="Are you eligible for work study?")
    ws_job              = models.ForeignKey(
                                            'WorkStudyJob',
                                            blank=True, null=True,,
                                            )
    clubs               = models.ManyToManyField(
                                            'Club',
                                            blank=True, null=True,
                                            )
    minority_caucus     = models.ManyToManyField(
											'MinorityCaucus',
                                            blank=True, null=True,
                                            )
    sports              = models.ManyToManyField(
                                            'Sport',
                                            blank=True, null=True,
                                            )
    societies           = models.ForeignKey(
                                            'Society',
                                            blank=True, null=True,
                                            )
    other_extra_curriculars=models.ManyToManyField(
                                            'ExtraCurricular',
                                            blank=True, null=True,
                                            )
    class_schedule      = models.OneToOneField(
                                            'Semester',
                                            blank=True, null=True,
                                            )
'''
