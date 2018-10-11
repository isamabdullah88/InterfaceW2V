import requests
from django import forms
from django.core.mail import mail_admins

from .models import *



class WordForm(forms.ModelForm):
    words = forms.ModelChoiceField(
        queryset=Word.objects.all(),
        widget=forms.Select(attrs={
            'class': 'browser-default',
        }))

    class Meta:
        model = Word
        fields = (
            'words',
        )

class ImageForm(forms.ModelForm):
    images = forms.ModelChoiceField(
        queryset=Image.objects.all(),
        widget=forms.Select(attrs={
            'class': 'browser-default',
        }))

    class Meta:
        model = Image
        fields = (
            'images',
        )