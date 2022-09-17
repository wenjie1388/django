"""
Django settings for cedar project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from ssl import Options
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(8g*j(f^nmohfu_+a=c9#=ch7)2n3e74se71dog77h_96y*z^^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 登录 URL 地址
LOGIN_URL = '/login'
ALLOWED_HOSTS = ['*', '127.0.0.1', 'example.com']
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']


# django 4.0新增配置
# CSRF_TRUSTED_ORIGINS = ['http://example.com']

# redis 配置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/9',
        # 'LOCATION': 'redis://username:password@127.0.0.1:6379/1',
        'TIMEOUT': 60*10,
        #  TIMEOUT 设置为 None ,永不过期; 0, 立即过期
        'Options': {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 缓存配置
# 控制 Django 存储会话数据的地方。包括的引擎有：
# 'django.contrib.sessions.backends.db'
# 'django.contrib.sessions.backends.file'
# 'django.contrib.sessions.backends.cache'
# 'django.contrib.sessions.backends.cached_db'
# 'django.contrib.sessions.backends.signed_cookies'
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# 默认： 'default'
# 如果你使用的是 基于缓存的会话存储，这将选择要使用的缓存
SESSION_CACHE_ALIAS = "default"


# 验证码配置
CAPTCHA_FLITE_PATH = None


# 跨域设置
# CORS_ORIGIN_ALLOW_ALL = True  # 允许所有的请求，或者设置CORS_ORIGIN_WHITELIST，二选一
CORS_ORIGIN_WHITELIST = [
    "http://localhost:5173",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5173",
]
'''CORS_ALLOWED_ORIGIN_REGEXES = [r"^https://\w+\.example\.com$",]'''
CORS_ALLOW_HEADERS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]  # '*' 允许所有的请求头
# 允许携带cookie，前端需要携带cookies访问后端时,需要设置withCredentials: true
CORS_ALLOW_CREDENTIALS = True


# 邮箱配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = os.environ.get('DJANGO_EMAIL_TLS', False)
EMAIL_USE_SSL = os.environ.get('DJANGO_EMAIL_SSL', True)
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.163.com')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 465)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',  # 处理跨域请求
    # 'article.apps.ArticleConfig',
    # 'testapp',
    # 'testapp.apps.TestappConfig',
    'article',  # 文章
    'account',  # 账号注册登录
    'oauth',    # 用户验证功能
    'captcha',
    'mdeditor',  # django-mdeditor 后台编辑器
]

# django-mdeditor 后端  ：https://gitee.com/pylixm/django-mdeditor/tree/master
X_FRAME_OPTIONS = 'SAMEORIGIN'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'  # 图片保存路径
MDEDITOR_CONFIGS = {
    'default': {
        'width': '90%',  # 自定义编辑框宽度
        'heigth': 500,   # 自定义编辑框高度
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                    "h1", "h2", "h3", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                    "emoji", "html-entities", "pagebreak", "goto-line", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"],  # 自定义编辑框工具栏
        # 图片上传格式类型
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
        'image_folder': 'editor',  # 图片保存文件夹名称
        'theme': 'default',  # 编辑框主题 ，dark / default
        'preview_theme': 'default',  # 预览区域主题， dark / default
        'editor_theme': 'default',  # edit区域主题，pastel-on-dark / default
        'toolbar_autofixed': True,  # 工具栏是否吸顶
        'search_replace': True,  # 是否开启查找替换
        'emoji': True,  # 是否开启表情功能
        'tex': True,  # 是否开启 tex 图表功能
        'flow_chart': True,  # 是否开启流程图功能
        'sequence': True,  # 是否开启序列图功能
        'watch': True,  # 实时预览
        'lineWrapping': False,  # 自动换行
        'lineNumbers': False  # 行号
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cedar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': [os.path.join(BASE_DIR, 'cedar-vue/dist')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cedar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DJANGO_MYSQL_DATABASE') or 'cedar',
        'USER': os.environ.get('DJANGO_MYSQL_USER') or 'root',
        'PASSWORD': os.environ.get('DJANGO_MYSQL_PASSWORD') or 'root',
        'HOST': os.environ.get('DJANGO_MYSQL_HOST') or '127.0.0.1',
        'PORT': int(
            os.environ.get('DJANGO_MYSQL_PORT') or 3306),
        'OPTIONS': {
            'charset': 'utf8mb4'},
    }

}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'account.BlogUser'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_URL = '/assets/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'cedar-vue/dist/assets')]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
