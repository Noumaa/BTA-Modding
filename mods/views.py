from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from mods.forms import ModSubmitForm
from mods.models import Mod, Version


# Create your views here.
def mods_list(request):
    return render(request, 'mods/list.html', {
        'mods': Mod.objects.all()
    })


@login_required
def mods_create(request):
    if request.method == "POST":
        form = ModSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            mod = form.save(commit=False)
            version = Version(
                label=form.cleaned_data['version_label'],
                file=form.cleaned_data['version_file'],
                mod=mod
            )
            mod.user = request.user
            mod.save()
            version.save()
    else:
        form = ModSubmitForm()
    return render(request, 'mods/create.html', {
        'form': form,
    })


def mods_detail(request, username, mod_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)
    return render(request, 'mods/detail.html', {
        'mod': mod,
        'versions': mod.versions.all(),
        'version': 'none'
    })


def version_download(request, username, mod_slug, version_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)
    version = get_object_or_404(Version, mod=mod, slug=version_slug)

    return render(request, 'mods/detail.html', {
        'mod': mod,
        'versions': mod.versions.all(),
        'version': version
    })
