__author__ = 'StriderKeni'

from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class Commentform(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
