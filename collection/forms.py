from django.forms import ModelForm

from collection.models import Thing
from django.forms import formset_factory
from django import forms

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name','branch','rollno','year' ,'description',)

   

