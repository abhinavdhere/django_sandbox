from django import forms

from .models import blogPost

class PostForm(forms.ModelForm):

    class Meta:
        model = blogPost
        fields = ('title', 'text',)
