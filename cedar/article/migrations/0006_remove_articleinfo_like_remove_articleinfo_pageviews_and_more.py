# Generated by Django 4.1 on 2022-09-15 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_articleinfo_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleinfo',
            name='like',
        ),
        migrations.RemoveField(
            model_name='articleinfo',
            name='pageviews',
        ),
        migrations.RemoveField(
            model_name='articleinfo',
            name='tags',
        ),
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(blank=True, default='0', verbose_name='点赞数'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='pageviews',
            field=models.IntegerField(blank=True, default='0', verbose_name='阅读量'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.JSONField(default='django开发', verbose_name='标签'),
            preserve_default=False,
        ),
    ]