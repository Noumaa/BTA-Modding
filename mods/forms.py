from django import forms
from django.forms import ModelForm

from mods.models import Mod, Version, Category, ExternalLinks, ReleaseChannel


def get_choices_for_category():
    choices = []
    for category in Category.objects.all():
        choices += [(category.pk, category.label)]
    return choices


class ModForm(ModelForm):
    categories = forms.MultipleChoiceField(required=True, choices=get_choices_for_category, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Mod
        exclude = ['slug', 'user', 'publish', 'views']


class ModSubmitForm(ModForm):
    version_label = forms.CharField()
    version_file = forms.FileField()
    version_release_channel = forms.ModelChoiceField(queryset=ReleaseChannel.objects.all())


class ModFilterForm(forms.Form):
    query = forms.CharField(required=False, widget=forms.TextInput(attrs={'type': 'hidden'}))
    categories = forms.MultipleChoiceField(required=False, choices=get_choices_for_category, widget=forms.CheckboxSelectMultiple)


class VersionSubmitForm(ModelForm):
    class Meta:
        model = Version
        exclude = ['slug', 'mod', 'publish', 'downloads']


class ExternalLinksForm(ModelForm):
    class Meta:
        model = ExternalLinks
        exclude = ['mod']
