from django import forms
from objects.models import CampusRoom

class CampusRoomForm(forms.ModelForm) :
	class Meta:
		model = CampusRoom
