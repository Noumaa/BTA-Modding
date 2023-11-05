from django.forms import ModelForm

from launcher.models import Launcher


class UploadLauncherForm(ModelForm):
    class Meta:
        model = Launcher
        fields = '__all__'
