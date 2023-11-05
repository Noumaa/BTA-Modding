from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from launcher.forms import UploadLauncherForm
from launcher.models import Launcher


def home(request):
    launcher = Launcher.objects.first()

    return render(request, "launcher/detail.html", {
        "latest_version": launcher
    })


@login_required
def upload(request):
    if not request.user.has_perm("launcher.add_launcher"):
        return redirect("launcher:detail")

    form = UploadLauncherForm()
    if request.method == "POST":
        form = UploadLauncherForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("launcher:detail")

    return render(request, "launcher/upload.html", {
        "form": form
    })


def api_version(request):
    launcher = Launcher.objects.first()
    if launcher is None:
        return JsonResponse({"code": 404, "message": "No launcher available."})

    return JsonResponse({
        "version": launcher.version,
        "url": launcher.file.url,
        "changelog": launcher.changelog,
        "published": launcher.published
    })
