from django.db import models
from django.utils.timezone import now
from django.utils.dateparse import parse_datetime
# Create your models here.

'''
用户校验表
'''
class OauthUser(models.Model):
    email = models.EmailField('email', max_length=100,blank=False,null=False)
    password = models.CharField('password',max_length=24,blank=False,null=False)
    # login_time = models.DateTimeField('login_time', default=now)

    

    def __str__(self):
        return self.email

        
    class Meta:
        db_table = 'oauthuser'
        ordering = ['-id']
        verbose_name = "用户校验表"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'