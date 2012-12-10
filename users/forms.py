from django import forms
from django.contrib.auth.models import User
from users.models import *
from objects.models import CampusArea

class InitRegForm(forms.Form) :
	uname = forms.CharField(
					label=(u'Please enter your my.whittier username'),
					max_length=8,
				)
	def clean_uname(self):
		uname = self.cleaned_data['uname']
		try :
			User.objects.get(username=uname)
		except User.DoesNotExist :
			return uname
		raise forms.ValidationError('Username already registered. Please contact site admins if this is a mistake.')

class MainRegForm(forms.ModelForm) :
#	NOTE: Fields to be validated with JS: 
#	all 3 phone fields, to ensure all filled if one filled
#	passwd fields
	fname = forms.CharField(max_length=30)
	lname = forms.CharField(max_length=50)
	passwd= forms.CharField(
					min_length=6,
					label=(u'Please select a password'), 
					widget=forms.PasswordInput(),
					error_messages={
						'min_length':'Your password must be at least 6 characters',
						'required':'Please choose a password',
					},

			)
	cfpass= forms.CharField(
					label=(u'Confirm password'),
					widget=forms.PasswordInput(),
				)
	area_code = forms.IntegerField(
			widget = forms.TextInput(
				attrs={
					'size':3,
					'maxlength':3,
					'onKeyPress':'return numbersOnly(this, event)',
				},
			),
			required=False,
	)
	phone_prefix = forms.IntegerField(
			widget = forms.TextInput(
				attrs={
					'size':3,
					'maxlength':3,
					'onKeyPress':'return numbersOnly(this, event)',
				},
			),
			required=False,
	)
	phone_suffix = forms.IntegerField(
			widget = forms.TextInput(
				attrs={
					'size':4,
					'maxlength':4,
					'onKeyPress':'return numbersOnly(this, event)',
				},
			),
			required=False,
	)
	residence = forms.ModelChoiceField(queryset=CampusArea.objects.filter(area_type='RH'))
	class Meta :
		model = SiteUser
		exclude = ('user','area_code','phone_prefix','phone_suffix','residence')
	def clean(self):
		passwd = self.cleaned_data.get('passwd')
		cfpass = self.cleaned_data.get('cfpass')
		if passwd != cfpass :
			raise forms.ValidationError('Passwords do not match. Please try again.')
		if self.cleaned_data.get('area_code') or self.cleaned_data.get('phone_prefix') or self.cleaned_data.get('phone_suffix') :
			if self.cleaned_data.get('area_code') and self.cleaned_data.get('phone_prefix') and self.cleaned_data.get('phone_suffix') :
				if (len(str(self.cleaned_data['area_code'])) != 3) or (len(str(self.cleaned_data['phone_prefix'])) != 3) or (len(str(self.cleaned_data['phone_suffix'])) != 4) :
					raise forms.ValidationError('The phone number you entered was not complete')
			else :
				raise forms.ValidationError('The phone number you entered was not complete')
		return self.cleaned_data

class ActivitiesProfileForm(forms.ModelForm) :
	class Meta:
		model = ActivitiesProfile
		exclude = ('user',)

class LoginForm(forms.Form) :
	uname = forms.CharField(max_length=8, label=(u'Username:'))
	passwd = forms.CharField(
					label=(u'Password:'), 
					widget=forms.PasswordInput(),
				)
