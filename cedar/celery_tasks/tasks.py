from celery import Celery
from django.core.mail import send_mail

import time
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedar.settings')
django.setup()
# 创建 celery 实例,名字一般是路径
app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/8')


@app.task
def send_register_email(email: str, url: str):
    '''
    发送注册邮件
    email: 请求邮箱
    url：注册链接
    '''
    subject = 'cedar账号邮箱绑定'
    message = '邮箱绑定~~'
    html_message = f"<p>恭喜您，您已经成功绑定您的邮箱，欢迎您继续关注本站，地址是</p><a href='{url}' rel='bookmark'>{url}</a>再次感谢您！<br />如果上面链接无法打开，请将以上链接复制至浏览器打开，有效期 <B>10</B> 分钟。"
    send_mail(subject, message, from_email=None,
              recipient_list=[email], html_message=html_message)
    time.sleep(3)
    '''
    subject: 一个字符串。邮件主题
    message: 一个字符串。
    from_email ：字符串。如果为 None ，Django 将使用 DEFAULT_FROM_EMAIL 设置的值。
    recipient_list: 一个字符串列表，每项都是一个邮箱地址。recipient_list 中的每个成员都可以在邮件的 "收件人:" 中看到其他的收件人。
    fail_silently: 一个布尔值。若为 False， send_mail() 会在发生错误时抛出 smtplib.SMTPException 。可在 smtplib 文档找到一系列可能的异常，它们都是 SMTPException 的子类。
    auth_user: 可选的用户名，用于验证登陆 SMTP 服务器。 若未提供，Django 会使用 EMAIL_HOST_USER 指定的值。
    auth_password: 可选的密码，用于验证登陆 SMTP 服务器。若未提供， Django 会使用 EMAIL_HOST_PASSWORD 指定的值。
    connection: 可选参数，发送邮件使用的后端。若未指定，则使用默认的后端。查询 邮件后端 文档获取更多细节。
    html_message: 若提供了 html_message，会使邮件成为 multipart/alternative 的实例， message 的内容类型则是 text/plain ，并且 html_message 的内容类型是 text/html 。
    message_type：1 注册激活
    '''
