from django import forms
from django.forms import ModelForm
from .models import Candidate, Position, Vresults



class CreateNewCandidate(ModelForm):
    class Meta:
        model = Candidate
        fields = ('image','title','position','body')
    # image=forms.ImageField(label='Profile Picture')
    # title=forms.CharField(label='Name', max_length=255)
    # position=forms.CharField(widget=forms.Select(choices = Positions))
    # body=forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder':'Write a brief introduction of yourself'}))
