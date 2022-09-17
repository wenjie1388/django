from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import widgets


from captcha.fields import CaptchaField

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.EmailInput(
            attrs={'placeholder': "支持邮箱", "class": "form-control",})
        self.fields['password'].widget = widgets.PasswordInput(
            attrs={'placeholder': "请输入密码", "class": "form-control"})
    
