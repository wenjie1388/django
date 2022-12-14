# Generated by Django 4.1 on 2022-09-14 19:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(help_text='标题', max_length=150, verbose_name='title')),
                ('authorid', models.CharField(max_length=50, verbose_name='作者ID')),
                ('author', models.CharField(help_text='作者', max_length=50, verbose_name='author')),
                ('content', mdeditor.fields.MDTextField(help_text='文章内容', verbose_name='content')),
                ('createdate', models.DateTimeField(default=django.utils.timezone.now, help_text='创建日期', verbose_name='createdate')),
                ('is_original', models.BooleanField(help_text='是否原创', verbose_name='is_original')),
                ('is_private', models.BooleanField(help_text='是否公开', verbose_name='is_private')),
                ('is_publish', models.BooleanField(help_text='是否发布', verbose_name='is_publish')),
            ],
            options={
                'db_table': 'Article',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ArticleInfo',
            fields=[
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='article.article')),
                ('updatedate', models.DateField(default=django.utils.timezone.now, help_text='更新日期', verbose_name='updatedate')),
                ('is_daleted', models.BooleanField(default=False, help_text='是否删除', verbose_name='is_daleted')),
                ('is_top', models.BooleanField(default=False, help_text='是否置顶', verbose_name='is_top')),
            ],
            options={
                'db_table': 'ArticleInfo',
                'ordering': ['-article'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenterid', models.IntegerField(blank=True, verbose_name='评论者id')),
                ('commenter', models.CharField(blank=True, max_length=16, verbose_name='评论者')),
                ('contents', models.CharField(blank=True, max_length=100, verbose_name='评论内容')),
                ('commentdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='评论时间')),
                ('respon', models.JSONField(max_length=255, null=True, verbose_name='回复内容')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article')),
            ],
            options={
                'db_table': 'Comment',
                'ordering': ['-article', '-commentdate'],
            },
        ),
    ]
