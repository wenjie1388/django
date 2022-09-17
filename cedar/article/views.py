

import json
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import View, ListView
from django.views.generic.edit import FormView
from django.urls import reverse

from typing import Any, Dict, Optional
from cedar.utils import LoginRequiredMixin
from article.forms import MDEditorModleForm
from article.models import Article, ArticleInfo, Comment
from account.models import BlogUser


class UserBlogView(LoginRequiredMixin, ListView):
    ''' 用户博客页面 '''
    template_name: str = 'user/blog.html'
    paginate_by = 5
    model = Article

    # def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     return render(request, self.template_name)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        content = super().get_context_data(**kwargs)
        return content

    def get_queryset(self):
        return super().get_queryset()


''' 文章页面 '''


class ArticleView(LoginRequiredMixin, View):
    template_name: str = 'user/article.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        articleid = kwargs.get('id')
        author = kwargs.get('author')

        # 获得 作者 信息
        author_obj = BlogUser.objects.get(username=author)

        # 获得 文章 信息
        article_obj = Article.objects.get(id=articleid)

        # 获得评论信息,没有评论的话则就为空
        try:
            comment_obj = Comment.objects.get(article_id=articleid)
            respons = json.loads(comment_obj.respon)
        except:
            comment_obj = None
            respons = None

        # 增加 阅读量 功能
        article_obj.pageviews += 1

        return render(request, self.template_name, {
            'article': article_obj,
            'author': author_obj,
            'comments': comment_obj,
            'respons': respons
        })


class MDEditorView(LoginRequiredMixin, FormView):
    ''' 编辑页面 '''

    template_name = 'user/mdeditor.html'
    form_class = MDEditorModleForm

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        ''' 获取数据 '''
        title = request.POST.get('title')
        content = request.POST.get('content')
        original = request.POST.get('is_original')
        private = request.POST.get('is_private')
        username = request.COOKIES.get('username')

        status = request.POST.get('btn-save', True)

        # 判断是草稿还是发布
        if status:
            ''' 发布 '''
            publish = True

        else:
            ''' 草稿 '''
            publish = False
        sessionid = request.COOKIES['sessionid']
        sessiondict = cache.get("django.contrib.sessions.cache"+sessionid)
        userid = sessiondict['_auth_user_id']
        username = BlogUser.objects.get(id=userid).username

        article = Article.objects.create(
            title=title,
            author=username,
            content=content,
            is_original=original,
            is_private=private,
            is_publish=publish
        )
        ArticleInfo.objects.create(
            article_id=article.id)
        return redirect(reverse('article:user'))
        # return redirect(reverse("article:mdeditor"))

    def form_valid(self, form) -> HttpResponse:
        # form.s
        return super().form_valid(form)
