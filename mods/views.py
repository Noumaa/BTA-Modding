from django.shortcuts import render, get_object_or_404

from mods.forms import ModSubmitForm
from mods.models import Mod


# Create your views here.
def mods_list(request):
    return render(request, 'mods/list.html', {
        'mods': Mod.objects.all()
    })


def mods_create(request):
    if request.method == "POST":
        form = ModSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ModSubmitForm()
    return render(request, 'mods/create.html', {
        'form': form,
    })


def mods_detail(request, mod_slug):
    return render(request, 'mods/detail.html', {
        'mod': get_object_or_404(Mod, pk=mod_slug)
    })
