from django import forms
from . import models

class Createlib(forms.ModelForm):
    class Meta:
        model = models.library_manager
        fields = ['topic_title' , 'slug' , 'overview' , 'img' ,'stored_file']

