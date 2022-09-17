
from typing import Any

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password


from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.utils import timezone
from django.urls import reverse
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.

from cedar.utils import LoginRequiredMixin

from .models import OauthUser


def testuser(request, username):
    data = {
        'username': username
    }
    return JsonResponse(data)


class UserProfile(LoginRequiredMixin, ListView):
    template_name: str = 'user/profile.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        return render(request, self.template_name)

    def get_queryset(self):
        return super().get_queryset()


class LogoutView(View):
    ''' 退出登录 '''

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        ''' 退出登录 '''
        # 清除用户信息，跳转首页
        logout(request)
        # request.session.set_test_cookie
        return redirect(reverse("index:index"))
