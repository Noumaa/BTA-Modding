from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from mods.forms import ModSubmitForm, ModEditForm
from mods.models import Mod, Version


# Create your views here.
def mods_list(request):
    mods = Mod.objects.all()
    query = request.GET.get('q')

    if query is not None:
        mods = mods.filter(Q(label__icontains=query) | Q(short_description__icontains=query))

    return render(request, 'mods/list.html', {
        'mods': mods
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

    messages.success(request, 'Starting download..')

    return render(request, 'mods/detail.html', {
        'mod': mod,
        'versions': mod.versions.all(),
        'version': version
    })


def mods_edit(request, username, mod_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)

    form = ModEditForm(instance=mod)
    if request.method == "POST":
        form = ModEditForm(request.POST, request.FILES, instance=mod)
        if form.is_valid():
            form.save()
            messages.success(request, "Settings edited!")
            return redirect('mods:detail', username=username, mod_slug=mod_slug)

    return render(request, 'mods/edit.html', {
        'mod': mod,
        'form': form
    })
