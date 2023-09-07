from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.urls import reverse_lazy

from mods.models import Mod
from users.forms import RegisterForm


# Create your views here.
class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('mods:list')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')  # TODO authenticate instand of redirect to login page

        messages.error(request, 'Invalid form ')
    else:
        form = RegisterForm()

    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render(request, 'registration/register.html', token)


def profile(request, username):
    target_user = get_object_or_404(User, username=username)

    downloads = 0
    for mod in Mod.objects.filter(user=target_user):
        downloads += mod.get_downloads()

    return render(request, 'users/profile.html', {
        'target_user': target_user,
        'downloads': downloads
    })
