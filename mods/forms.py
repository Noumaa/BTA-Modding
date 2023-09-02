from django import forms
from django.forms import ModelForm

from mods.models import Mod


class ModSubmitForm(ModelForm):
    version_label = forms.CharField()
    version_file = forms.FileField()

    class Meta:
        model = Mod
        exclude = ['slug', 'user', 'publish']


class ModEditForm(ModelForm):
    class Meta:
        model = Mod
        exclude = ['slug', 'user', 'publish']
