from django.forms import ModelForm

from mods.models import Mod


class ModSubmitForm(ModelForm):
    class Meta:
        model = Mod
        exclude = []
