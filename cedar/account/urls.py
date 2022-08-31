from django.urls import path,re_path

from .forms import LoginForm
from . import views
app_name = "account"

urlpatterns = [
    path('login',
    views.LoginView.as_view(),
    name='login',
    kwargs={'authentication_form': LoginForm}),
]