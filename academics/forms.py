from django import forms
from academics.models import *

class BookForm(forms.ModelForm) :
	class Meta :
		model = Book
		exclude = ('book_seller',)

class ClassForm(forms.ModelForm) :
	class Meta :
		model = AcademicClass

class AcDeptForm(forms.ModelForm) :
	class Meta :
		model = AcademicDept

class ProfForm(forms.ModelForm) :
	class Meta :
		model = Professor

class ClassProfileForm(forms.ModelForm) :
	class Meta :
		model = AcademicClassProfile
