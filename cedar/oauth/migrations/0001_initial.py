# Generated by Django 4.1 on 2022-08-31 12:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OauthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('password', models.CharField(max_length=24, verbose_name='password')),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='login_time')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last_mod_time')),
            ],
            options={
                'db_table': 'oauthuser',
            },
        ),
    ]