from django import forms
from moviesapp.models import Movies
class Movieform(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['name','desc','year','image']

