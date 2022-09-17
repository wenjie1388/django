from django.contrib import admin
from .models import Article, ArticleInfo,Comment
# Register your models here.

admin.site.register([Article, ArticleInfo, Comment])
