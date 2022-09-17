

from mdeditor.fields import MDTextFormField
from django import forms
from django.forms import ModelForm


# from article.models import ArticleInfo

# ModelForm 将对照 model 创建表单，参考：https://docs.djangoproject.com/zh-hans/4.1/topics/forms/modelforms/#field-types


class MDEditorModleForm(forms.Form):

    title = forms.CharField(label='')
    content = MDTextFormField(label='')
    is_original = forms.ChoiceField(
        choices=[(True, '原创'), (False, '转载')], label='',)
    is_private = forms.ChoiceField(
        choices=[(True, '所有人可见'), (False, '仅自己可见')], label='')
    #


# class InfoModelForm(ModelForm):
#     ''' Article Info '''

#     class Meta:
#         model = ArticleInfo
#         fields = ['is_original', 'is_private',
#                   'is_top', 'is_daleted', 'is_publish']
