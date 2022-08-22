import logging
from django.shortcuts import render
from django.views.generic.list import ListView
from django.core.cache import cache

# Create your views here.

# from djangoblog.utils import cache, get_sha256, get_blog_setting

logger = logging.getLogger(__name__)

class IndexViews(ListView):
    # template_name属性用于指定使用哪个模板进行渲染
    template_name = 'index/index.html'

    

    def get_queryset(self):
        '''
        重写默认，从缓存获取数据
        :return:
        '''
        # key = self.get_queryset_cache_key()
        # value = self.get_queryset_from_cache(key)
        # return value    
        return None
