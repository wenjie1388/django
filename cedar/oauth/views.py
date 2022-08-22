from msilib.schema import ListView
from django.shortcuts import render

# Create your views here.


class LoginView(ListView):

    template_name = 'oauth/login.html'
