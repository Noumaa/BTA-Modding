from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import User
from django.db.models import Q, Max
from django.shortcuts import render, get_object_or_404, redirect

from mods.forms import ModSubmitForm, ModForm, VersionSubmitForm
from mods.models import Mod, Version


# Create your views here.
def mods_list(request):
    mods = Mod.objects.all()
    query = request.GET.get('q')

    if query is not None:
        mods = mods.filter(Q(label__icontains=query) | Q(short_description__icontains=query))

    mods = mods \
        .annotate(last_version_publish=Max('versions__publish')) \
        .order_by('-last_version_publish')

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

            return redirect('mods:detail', username=request.user.username, mod_slug=mod.slug)

    else:
        form = ModSubmitForm()

    return render(request, 'mods/create.html', {
        'form': form,
    })


def mods_detail(request, username, mod_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)

    mod.views += 1
    mod.save()

    return render(request, 'mods/detail.html', {
        'mod': mod,
        'versions': mod.versions.all(),
        'version': 'none'
    })


@login_required
def mods_edit(request, username, mod_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)

    form = ModForm(instance=mod)
    if request.method == "POST":
        form = ModForm(request.POST, request.FILES, instance=mod)
        if form.is_valid():
            form.save()
            messages.success(request, "Settings edited!")
            return redirect('mods:detail', username=username, mod_slug=mod_slug)

    return render(request, 'mods/edit.html', {
        'mod': mod,
        'form': form
    })


def version_list(request, username, mod_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)

    return render(request, 'mods/version-list.html', {
        'mod': mod,
        'versions': mod.versions.all(),
    })


def version_detail(request, username, mod_slug, version_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)
    version = get_object_or_404(Version, mod=mod, slug=version_slug)

    return render(request, 'mods/version-detail.html', {
        'mod': mod,
        'version': version,
        'versions': mod.versions.all(),
    })


@login_required
def version_create(request, username, mod_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)

    form = VersionSubmitForm()
    if request.method == "POST":
        form = VersionSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            version = form.save(commit=False)
            version.mod = mod
            version.save()

            messages.success(request, "Mod updated!")
            return redirect('mods:version-detail', username=username, mod_slug=mod_slug, version_slug=version.slug)

    return render(request, 'mods/version-create.html', {
        'mod': mod,
        'form': form,
        'versions': mod.versions.all(),
    })


def version_download(request, username, mod_slug, version_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)
    version = get_object_or_404(Version, mod=mod, slug=version_slug)

    version.downloads += 1
    version.save()

    return render(request, 'mods/version-download.html', {
        'mod': mod,
        'version': version,
        'versions': mod.versions.all(),
    })
