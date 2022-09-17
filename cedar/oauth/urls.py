from django.contrib.auth.decorators import login_required
from django.urls import re_path, path
from . import views


app_name = 'oauth'

urlpatterns = [

    re_path(r'^user/(?P<username>.*)$',
            views.testuser),

    re_path('^user/profile$',
            views.UserProfile.as_view(),
            #     login_required(views.UserCenter.as_view()),
            name='profile'),

    re_path(r'^logout/$',
            views.LogoutView.as_view(),
            name='logout',),
]
