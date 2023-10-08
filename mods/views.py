from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from mods.forms import ModForm, VersionSubmitForm, ModFilterForm, ExternalLinksForm, ModSubmitForm
from mods.models import Mod, Version, GameVersion
from users.models import User


class ModListView(ListView):
    model = Mod
    paginate_by = 10

    def get_queryset(self):
        mods = Mod.objects.all()
        form = ModFilterForm(self.request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            categories = form.cleaned_data['categories']

            if query:
                mods = mods.filter(Q(label__icontains=query) | Q(short_description__icontains=query))

            if categories:
                mods = mods.filter(categories__in=categories)

        mods = mods \
            .annotate(last_version_publish=Max('versions__publish')) \
            .order_by('-last_version_publish')

        return mods

    def get_context_data(self, **kwargs):
        form = ModFilterForm(self.request.GET)

        context = super().get_context_data(**kwargs)
        context['form'] = form
        context['meta_description'] = 'Search and browse thousands of Minecraft Mods on BTA Modding with instant, accurate search results. Our filters help you quickly find the best Minecraft Mods for Better Than Adventure!'
        return context


@login_required
def mods_create(request):
    mod_form = ModSubmitForm()
    links_form = ExternalLinksForm()

    if request.method == "POST":
        mod_form = ModSubmitForm(request.POST, request.FILES)
        links_form = ExternalLinksForm(request.POST)

        if mod_form.is_valid() and links_form.is_valid():
            mod = mod_form.save(commit=False)
            mod.user = request.user
            mod.save()

            version = Version(
                mod=mod,
                label=mod_form.cleaned_data['version_label'],
                file=mod_form.cleaned_data['version_file'],
                release_channel=mod_form.cleaned_data['version_release_channel'],
                game_version=mod_form.cleaned_data['version_game_version'],
            )
            version.save()

            for loader in mod_form.cleaned_data['version_loaders']:
                version.loaders.add(loader.pk)

            links = links_form.save(commit=False)
            links.mod = mod
            links.save()

            mod_form.save_m2m()

            return redirect('mods:detail', username=request.user.username, mod_slug=mod.slug)

    game_versions = [[version.pk, version.label] for version in GameVersion.objects.all()]

    return render(request, 'mods/create.html', {
        'form': mod_form,
        'links_form': links_form,
        'game_versions': game_versions,
    })


def mods_detail(request, username, mod_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)

    mod.views += 1
    mod.save()

    return render(request, 'mods/detail.html', {
        'mod': mod,
        'versions': mod.versions.all(),
        'version': 'none',
        'meta_title': mod.label + ' - Minecraft Mod',
        'meta_description': mod.short_description,
        'meta_image': mod.logo.url,
    })


@login_required
def mods_edit(request, username, mod_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)

    if mod.user != request.user:
        messages.error(request, 'Can\'t edit other resources!')
        return redirect('mods:detail', username, mod_slug)

    form = ModForm(instance=mod)

    links_form = ExternalLinksForm()
    if mod.links.exists():
        links_form = ExternalLinksForm(instance=mod.links.first())

    if request.method == "POST":
        form = ModForm(request.POST, request.FILES, instance=mod)
        links_form = ExternalLinksForm(request.POST, instance=mod.links.first())
        if form.is_valid() and links_form.is_valid():
            form.save()

            links = links_form.save(commit=False)
            links.mod = mod
            links.save()

            messages.success(request, "Settings edited!")
            return redirect('mods:detail', username=username, mod_slug=mod_slug)

    return render(request, 'mods/edit.html', {
        'mod': mod,
        'form': form,
        'links_form': links_form
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

    if mod.user != request.user:
        messages.error(request, 'Can\'t edit other resources!')
        return redirect('mods:detail', username, mod_slug)

    form = VersionSubmitForm()
    if request.method == "POST":
        form = VersionSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            version = form.save(commit=False)
            version.mod = mod
            version.save()

            form.save_m2m()

            messages.success(request, "Mod updated!")
            return redirect('mods:version-detail', username=username, mod_slug=mod_slug, version_slug=version.slug)

    game_versions = [[version.pk, version.label] for version in GameVersion.objects.all()]

    return render(request, 'mods/version-create.html', {
        'mod': mod,
        'form': form,
        'versions': mod.versions.all(),
        'game_versions': game_versions,
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


@login_required
def mods_setting(request, username, mod_slug):
    user = get_object_or_404(User, username=username)
    mod = get_object_or_404(Mod, slug=mod_slug, user=user)

    if mod.user != request.user:
        messages.error(request, 'Can\'t edit other resources!')
        return redirect('mods:detail', username, mod_slug)

    return render(request, 'mods/settings.html', {
        'mod': mod,
    })
