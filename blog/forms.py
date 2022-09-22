"""
forms are defined here
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    commentform is defined here
    """
    class Meta:
        """
        defined meta data on this class
        """
        model = Comment
        fields = ('body',)
