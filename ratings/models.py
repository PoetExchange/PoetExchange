#####################
# MODEL DEPENDENCIES
#####################
# -------------------
# DEPENDS ON: 'users' app
# -------------------
# ProfRatingsTable
# -------------------
# DEPENDS ON: 'academics' app
# -------------------
# ProfRatingsTable

from django.db import models

# Create your models here.
class ProfRatingsTable(models.Model) :
	professor			= models.ForeignKey('academics.Professor')
	user				= models.ForeignKey('users.User')
	rating				= models.IntegerField(
											choices=(
												(-1, '-1'),
												(0, '0'),
												(1, '+1'),
												),
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
		code = int("%d%d" % (self.professor.pk, self.user.pk))
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
