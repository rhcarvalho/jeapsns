from django import forms

from jeapsns.models import post


class PostForm(forms.ModelForm):
    # :=> MODEL => Django creates a form automatically
    class Meta:
        model = post
        fields = ('content',)
        
    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) == 0:
            raise forms.ValidationError("Empty!")
        return content
