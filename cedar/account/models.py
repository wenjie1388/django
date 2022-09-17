from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.utils.functional import lazy

# from cedar.utils import get_current_site


# 验证器，除了 @、.、+、- 和 _ 之外，还允许使用 Unicode 字符的字段验证器
Unicode_validator = UnicodeUsernameValidator()
# ASCIIUsernameValidator ：除了 @、.、+、- 和 _ 之外，只允许使用 ASCII 字母和数字的字段验证器
ASCII_validator = ASCIIUsernameValidator()


class BlogUser(AbstractUser):

    photo = models.ImageField(
        'photo',
        height_field=150,
        width_field=100,
        blank=True,
    )
    mobile = models.CharField(
        'mobile',
        max_length=11,
        help_text=('仅限11位数字'),
        error_messages={'unique': ("手机号格式不正确")},
        blank=True,
    )

    name = models.CharField(
        'name',
        max_length=10,
        blank=True,
    )

    idcard = models.CharField(
        'idcard',
        max_length=18,
        blank=True,
        validators=[ASCII_validator],
        error_messages={'unique': "身份证格式不正确"}
    )

    username = models.CharField(
        'username',
        max_length=16,
        unique=True,
        help_text=(
            '支持 16个字符，汉字、数字、字母以及特殊符号(@/./+/-/_)。'),
        validators=[Unicode_validator],
        error_messages={
            'unique': ("用户名已存在."),
        },
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = "user"
        verbose_name_plural = verbose_name
        db_table = 'user'
