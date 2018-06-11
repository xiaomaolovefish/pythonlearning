from django import forms
from django.contrib import admin
 
class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
class Shares(forms.Form):
    name = forms.CharField(max_length=100)
    adress = forms.CharField(max_length=100)
    price = forms.CharField(max_length=3)
    detail = forms.CharField(max_length=100)
   # InputFile = forms.ImageField() 
class search_list(forms.Form):
    q = forms.CharField(max_length=100)

from django.contrib.auth.models import User

from models import Profile

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('created_by',)

  
class GalleryAdminForm(forms.Form):
    name = forms.CharField(max_length=100)
    adress = forms.CharField(max_length=100)
    price = forms.CharField(max_length=3)
    detail = forms.CharField(max_length=100)
