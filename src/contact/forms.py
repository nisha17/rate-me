from django import forms
from django.forms import ModelForm, Textarea, TextInput



class ContactForm(forms.Form):
	full_name = forms.CharField(required = False, max_length=120)
	email = forms.EmailField(required=True, help_text='Please enter a valid email address')
	message = forms.CharField(required=True,widget=forms.Textarea)

