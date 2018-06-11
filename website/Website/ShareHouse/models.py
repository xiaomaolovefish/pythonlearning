from __future__ import unicode_literals

from django.db import models

from django.contrib import admin

from django.forms import ModelForm
from django import forms

from django.utils.translation import ugettext_lazy as _

from users.models import User



class ShareH(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    price = models.CharField(max_length=3)
    detail = models.CharField(max_length=100)
    InputFile = models.ImageField(upload_to='photos') 
    #submit_date = models.DateField(blank=True, null=True)



    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
    

    
admin.site.register(ShareH)


class ShareHForm(ModelForm):
    class Meta:
        model = ShareH
        #fields = ['name', 'adress', 'price','detail']
        fields='__all__'
        widgets={'name':forms.TextInput(attrs={'class': 'special','style':"width:100%"}),'detail':forms.TextInput(attrs={'size': '100','style':"width:100%", 'rows':25}),'price':forms.TextInput(attrs={'class': 'special','style':"width:100%"}),'adress':forms.TextInput(attrs={'class': 'special','style':"width:100%"}),}
        InputFile = forms.ImageField(required=False)  
class ShareForm(ModelForm):
    class Meta:
        model = ShareH

        fields='__all__'
       


class Profile(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='imgs')
   

    created_by = models.ForeignKey(User)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
    
admin.site.register(Profile)



