from django import forms
from django.contrib.auth.models import User
from users.models import *

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
	fname = forms.CharField(max_length=30)
	lname = forms.CharField(max_length=50)
	passwd= forms.CharField(
					label=(u'Please select a password'), 
					widget=forms.PasswordInput(),
				)
	cfpass= forms.CharField(
					label=(u'Confirm password'),
					widget=forms.PasswordInput(),
				)
	class Meta :
		model = SiteUser
		exclude = ('user',)
	def clean(self):
		passwd = self.cleaned_data['passwd']
		cfpass = self.cleaned_data['cfpass']
		if passwd != cfpass :
			raise forms.ValidationError('Passwords do not match. Please try again.')
		return self.cleaned_data
