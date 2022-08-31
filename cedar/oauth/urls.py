from django.urls import re_path,path
from . import views

app_name = 'oauth'

urlpatterns = [
    path('user',views.OauthLogin.as_view(),name='oauthlogin')
]
