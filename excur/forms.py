from django import forms
from excur.models import *
from objects.models import *
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

class ExtrCurProfileForm(forms.ModelForm) :
#NOTE: Form is being manually constructed by combining fields of the three different profile Construct all varying fields in different formsets, similar fields in the same formset.
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
	semester			= forms.ModelChoiceField(
									queryset=Semester.objects.all(),
									empty_label="(Select semester...)"),
									required=False,
	year				= IntegerField(
									max_value=2100, 
									label=(u'Year:'),
									required=False,
								)
	soc_group			= forms.ModelChoiceField(
									queryset=Society.objects.all(), 
									empty_label="(Select Society...)",
									required=False,
								)
	sport_group			= forms.ModelChoiceField(
									queryset=Sport.objects.all(),
									empty_label="(Select Sport...)",
									required=False,
								)
	excur_group			= forms.ModelChoiceField(
									queryset=ExtraCurricular.objects.all(),
									empty_label="(Select group...),"
									required=False,
								)
	excur_mtgDays		= forms.ModelMultipleChoiceField(
									queryset=WeekDay.objects.all(),
									empty_label="(Select meeting day...)",
									required=False,
								)
	excur_mtgTime		= forms.TimeField(required=False)
	excur_mtgArea		= forms.ModelChoiceField(
									queryset=CampusArea.objects.all(),
									empty_label="(Select meeting area...)",
									required=False,
								)
	excur_mtgRoom		= forms.ModelChoiceField(
									queryset=CampusRoom.objects.all(),
									empty_label="(Select meeting room...)",
									required=False,
								)

class ExtrCurOfficerForm(form.ModelForm) :
	class Meta :
		model = ExtrCurOfficer

class TeamCaptForm(form.ModelForm) :
	class Meta :
		model = TeamCapt
