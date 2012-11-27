from django import forms
from excur.models import *
from django.core.validators import MaxLengthValidator
# NOTE: Following forms will need JS validation:
# ExtraCurricularForm to show appropriate fields depending on group type chosen
# ExtrCurOfficerForm, reasons stated ^^

class AdDepartmentForm(forms.ModelForm) :
	class Meta :
		model = AdministrativeDepartment

class WorkStudyJobForm(forms.ModelForm) :
	class Meta :
		model = WorkStudyJob

class ExtraCurricularForm(forms.ModelForm) :
	group_type			= forms.CharField(
									max_length=2,
									choices=(
										('SP', 'Sport'),
										('SC', 'Society'),
										('CB','Club'),
										('MC','Minority Caucus'),
										('SG','Student Government'),
										('SM','Student Media'),
										('HS','Honors Society'),
										('OR','Other'),
									),
								)
	group_name = forms.CharField(max_length=30)
	soc_group_name = forms.CharField(max_length=12)
	group_description = forms.TextField(
									validators=[MaxLengthValidator(500)]
								)
	is_active = forms.BooleanField(default=True)
		class Meta :
			model = Sport

# class ExtrCurProfileForm(forms.ModelForm) :
#	This one is gonna be a bitch... maybe just make 3 separate profile forms

class ExtrCurOfficerForm(form.ModelForm) :
	class Meta :
		model = ExtrCurOfficer

class TeamCaptForm(form.ModelForm) :
	class Meta :
		model = TeamCapt
		exclude = ('user',)
