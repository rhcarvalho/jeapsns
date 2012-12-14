from django import forms

class postForm(forms.Form):
	content=forms.CharField(label="",widget=forms.Textarea)
