
''' 验证码组件 '''
from captcha.models import CaptchaStore
from captcha.helpers import captcha_audio_url, captcha_image_url

from django.conf import settings
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password, check_password

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView, ListView

import re
from typing import Any, Dict, List
import json
import logging

from .models import BlogUser
from article.models import Article, ArticleInfo

from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from celery_tasks.tasks import send_register_email

logger = logging.getLogger(__name__)

# Create your views here.


class IndexViews(ListView):
    # template_name属性用于指定使用哪个模板进行渲染
    template_name = 'index/index.html'
    paginate_by = 5
    model = Article

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        article = Article.objects.order_by('-like')
        return render(request, self.template_name, {
            'articles': article
        })
    # return render(request, self.template_name)

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context = Article.objects.order_by('-like')
    #     return context

    # def get_queryset(self):
    #     article = Article.objects.order_by('-like')
    #     return article


class LoginView(ListView):
    ''' 用户登录 '''
    template_name = 'account/login.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # 接收用户数据
        username = request.GET.get('username')
        password = request.GET.get('password')
        captcha = request.GET.get('captcha')
        print(username, password)
        # 完整性校验
        if not all([username, password, captcha]):
            return render(request, self.template_name)

        # 用户名和密码校验
        user = authenticate(username=username, password=password)
        if user is None:
            # 用户名密码错误或未激活
            context = {
                'Status Code': 200,
                # "errmsg":'用户未激活，请返回邮箱激活；若仍未收到邮箱请检查邮箱是否错误或反馈给管理员'
                'errmsg': '用户名密码错误或未激活！',
            }
            return render(request, self.template_name, context)
        # 保存登录状态
        login(request, user)

        next_url = request.GET.get("next")
        if next_url != None:
            return redirect(reverse(f'oauth:{next_url}'))

        # response.set.COOKIES = {}
        response = redirect(reverse("account:index"))
        return response

    def get_queryset(self, request):
        # username = request.COOKIES.get('username')
        sessionid = request.GET.get('sessionid')
        # return render(request, self.template_name, {'sessionid': sessionid})
        return None


class RegisterView(ListView):
    ''' 用户注册 '''
    template_name = 'account/register.html'

    def get_queryset(self):

        return None

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # 接收用户数据
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        checkcode = request.POST.get('checkcode')
        allow = request.POST.get('allow')

        # 数据校验
        if not all([username, password1, password2, email, checkcode]):
            context = {
                'Status Code': 205,
                "errmsg": '数据不完整',
            }
            return render(request, self.template_name, context)

        # 密码校验
        if password1 != password2:
            context = {
                'Status Code': 205,
                "errmsg_pw": "密码错误",
            }
            return render(request, self.template_name, context)

        # 邮箱校验
        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9_-]+)+$', email):
            context = {
                'Status Code': 205,
                "errmsg_em": "邮箱错误",
            }
            return render(request, self.template_name, context)

        # 验证码校验
        if checkcode != '1234':
            return render(request, self.template_name, {"errmsg_ch": "验证码错误"})

        # 协议校验
        if allow != 'on':
            return render(request, self.template_name, {"errmsg_al": "请同意协议"})

        # 注册业务处理
        try:
            BlogUser.objects.get(username=username)
            return render(request, self.template_name, {"errmsg_us": "用户名已存在"})
        except BlogUser.DoesNotExist:
            # 注册成功
            BlogUser.objects.create_user(
                username=username, password=password1, email=email, is_active=0)
            user = BlogUser.objects.get(username=username)
        # 发送激活链接  http://127.0.0.1:8000/user/active/$id$username
        # 加密生成 token
            urlserializer = URLSafeTimedSerializer(settings.SECRET_KEY)
            token = urlserializer.dumps({'id': user.id, })
        # 发送邮件
            url = 'http://127.0.0.1:8000/user/active/' + token
            send_register_email.delay(url=url, email=email)

        # 返回应答
            # return redirect(reverse("index:index"))
            return render(request, 'succeeded\send_mail.html')


class ActiveView(ListView):
    '''用户激活'''

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        token = kwargs["token"]
        urlserializer = URLSafeTimedSerializer(settings.SECRET_KEY)
        try:
            # 验证 token
            user_info = urlserializer.loads(token, max_age=60*10)

            # 获取用户
            id = user_info.get('id', None)
            # username = user.get('username',None)
            user = BlogUser.objects.get(id=id)
            user.is_active = 1
            user.save()

            # 跳转登录页面
            return redirect(reverse("account:login"))
        except SignatureExpired:
            return HttpResponse("已经过期")
