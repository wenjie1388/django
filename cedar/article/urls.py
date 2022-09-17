from django.urls import path, re_path
from . import views


app_name = "article"

urlpatterns = [
    re_path(r'^user/$',
            views.UserBlogView.as_view(),
            name='user'),

    re_path(r'^user/(?P<author>.*)/article/(?P<id>.*)$',
            views.ArticleView.as_view(),
            name='article'),

    re_path(r'^user/mdeditor/$',
            views.MDEditorView.as_view(),
            name='mdeditor'),
]
