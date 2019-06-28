from django import forms
from .models import Todo
from django.contrib.auth.models import User


class AddNew(forms.ModelForm):
	task = forms.CharField( widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}))
	class Meta:
		model = Todo
		fields= ('task','priority')