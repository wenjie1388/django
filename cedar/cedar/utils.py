from email import message
import logging
import os
import random
import string
import uuid
from hashlib import sha256

# import markdown
# import requests
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.core.mail import send_mail, send_mass_mail

# from

logger = logging.getLogger(__name__)


class LoginRequiredMixin(object):
    ''' 登录验证 多继承 Mixin '''
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def get_sha256(str):
    m = sha256(str.encode('utf-8'))
    return m.hexdigest()


'''
def generate_code() -> str:
    """生成随机数验证码"""
    return ''.join(random.sample(string.digits, 6))


def parse_dict_to_url(dict):
    from urllib.parse import quote
    url = '&'.join(['{}={}'.format(quote(k, safe='/'), quote(v, safe='/'))
                    for k, v in dict.items()])
    return url


def get_blog_setting():
    value = cache.get('get_blog_setting')
    if value:
        return value
    else:
        from blog.models import BlogSettings
        if not BlogSettings.objects.count():
            setting = BlogSettings()
            setting.sitename = 'djangoblog'
            setting.site_description = '基于Django的博客系统'
            setting.site_seo_description = '基于Django的博客系统'
            setting.site_keywords = 'Django,Python'
            setting.article_sub_length = 300
            setting.sidebar_article_count = 10
            setting.sidebar_comment_count = 5
            setting.show_google_adsense = False
            setting.open_site_comment = True
            setting.analyticscode = ''
            setting.beiancode = ''
            setting.show_gongan_code = False
            setting.save()
        value = BlogSettings.objects.first()
        logger.info('set cache get_blog_setting')
        cache.set('get_blog_setting', value)
        return value


def save_user_avatar(url):

    # 保存用户头像
    # :param url:头像url
    # :return: 本地路径
    setting = get_blog_setting()
    logger.info(url)

    try:
        imgname = url.split('/')[-1]
        if imgname:
            path = r'{basedir}/avatar/{img}'.format(
                basedir=setting.resource_path, img=imgname)
            if os.path.exists(path):
                os.remove(path)
        rsp = requests.get(url, timeout=2)
        if rsp.status_code == 200:
            basepath = r'{basedir}/avatar/'.format(
                basedir=setting.resource_path)
            if not os.path.exists(basepath):
                os.makedirs(basepath)

            imgextensions = ['.jpg', '.png', 'jpeg', '.gif']
            isimage = len([i for i in imgextensions if url.endswith(i)]) > 0
            ext = os.path.splitext(url)[1] if isimage else '.jpg'
            savefilename = str(uuid.uuid4().hex) + ext
            logger.info('保存用户头像:' + basepath + savefilename)
            with open(basepath + savefilename, 'wb+') as file:
                file.write(rsp.content)
            return 'https://resource.lylinux.net/avatar/' + savefilename
    except Exception as e:
        logger.error(e)
        return url


def delete_sidebar_cache():
    from blog.models import LinkShowType
    keys = ["sidebar" + x for x in LinkShowType.values]
    for k in keys:
        logger.info('delete sidebar key:' + k)
        cache.delete(k)


def delete_view_cache(prefix, keys):
    from django.core.cache.utils import make_template_fragment_key
    key = make_template_fragment_key(prefix, keys)
    cache.delete(key)
'''
