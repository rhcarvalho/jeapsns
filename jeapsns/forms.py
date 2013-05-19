from django import forms

from jeapsns.models import post


class postForm(forms.Form):
	content=forms.CharField(label="",widget=forms.Textarea)


class PostForm(forms.ModelForm):
    class Meta:
        model = post

