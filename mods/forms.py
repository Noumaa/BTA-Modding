from django import forms
from django.forms import ModelForm

from mods.models import Mod, Version


class ModForm(ModelForm):
    class Meta:
        model = Mod
        exclude = ['slug', 'user', 'publish', 'views']


class ModSubmitForm(ModForm):
    version_label = forms.CharField()
    version_file = forms.FileField()


class ModFilterForm(forms.Form):
    query = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Rechercher un mod'}))
    categories = forms.MultipleChoiceField(required=False, choices=Mod.Categories.choices)


class VersionSubmitForm(ModelForm):
    class Meta:
        model = Version
        exclude = ['slug', 'mod', 'publish']
