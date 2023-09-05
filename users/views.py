from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.urls import reverse_lazy

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
