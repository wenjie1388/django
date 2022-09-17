from django.conf import settings
from django.conf.urls.static import static
# from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include


urlpatterns = [
    re_path(r'', include('account.urls', namespace='account')),
    re_path(r'', include('article.urls', namespace='articles')),
    re_path(r'', include('oauth.urls', namespace='oauth')),
    # re_path(r'test/', include('testapp.urls')),
    # re_path(r'', login_required(include('oauth.urls', namespace='oauth'))),

    re_path(r'mdeditor/', include('mdeditor.urls')),
    path(r'captcha/', include('captcha.urls')),
    # path('admin/', admin.site.urls),
]

if settings.DEBUG:
    ''' 开发时提供静态文件服务,但不适合生产环境，参考：https://docs.djangoproject.com/zh-hans/4.1/howto/static-files/deployment/'''
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
