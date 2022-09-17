
from logging import NullHandler
from re import T
from statistics import mode
from urllib import response
from django.utils import timezone
# from datetime import datetime, timedelta, timezone, tzinfo
# from django.contrib.auth import now
from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.

''' 文章表 '''


class Article(models.Model):

    id = models.AutoField('id', primary_key=True)
    title = models.CharField('title', max_length=150, help_text='标题')
    authorid = models.CharField('作者ID', max_length=50)
    author = models.CharField('author', max_length=50, help_text='作者')
    content = MDTextField(verbose_name='content', help_text='文章内容')
    createdate = models.DateTimeField(
        'createdate', default=timezone.now, help_text='创建日期')
    is_original = models.BooleanField(
        'is_original', help_text='是否原创')
    is_private = models.BooleanField(
        'is_private',  help_text='是否公开')
    is_publish = models.BooleanField(
        'is_publish', help_text='是否发布')
    tags = models.JSONField('标签')
    like = models.IntegerField('点赞数', blank=True)
    pageviews = models.IntegerField('阅读量', blank=True)

    def __str__(self) -> str:
        return "ID:%s .标题：%s" % (self.id, self.title)
        # return self.title

    class Meta:
        ordering = ['-id']
        db_table = 'Article'


''' 文章信息表 '''


class ArticleInfo(models.Model):

    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, primary_key=True)
    updatedate = models.DateField(
        'updatedate', default=timezone.now, help_text='更新日期')
    is_daleted = models.BooleanField(
        'is_daleted', default=False, help_text='是否删除')
    is_top = models.BooleanField('is_top', default=False, help_text='是否置顶')

    def __str__(self) -> str:
        # return f"ID:{self.blogid},创建人:{self.createby}."
        return (f"self.article_id：{self.article_id}")

    class Meta:
        ''' 元数据选项'''
        # 对象的默认排序，用于获取对象列表时
        ordering = ['-article_id']
        db_table = 'ArticleInfo'


class Comment(models.Model):
    ''' 评论表 '''
    article = models.ForeignKey(
        'article', on_delete=models.CASCADE)
    commenterid = models.IntegerField('评论者id', blank=True)
    commenter = models.CharField('评论者', blank=True, max_length=16)
    contents = models.CharField('评论内容', blank=True, max_length=100)
    commentdate = models.DateTimeField('评论时间', default=timezone.now,)
    respon = models.JSONField('回复内容', max_length=255, null=True)

    def __str__(self) -> str:
        return self.commenter

    class Meta:
        ordering = ['-article', '-commentdate']
        db_table = 'Comment'
