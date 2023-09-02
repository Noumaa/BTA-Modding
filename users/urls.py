from django.contrib.auth.views import LogoutView
from django.urls import path

from users import views
from users.views import MyLoginView

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
]
