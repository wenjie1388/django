def send_verify_email(to_mail: str, code: str, subject: str = "邮件验证码"):
    """发送重设密码验证码
    Args:
        to_mail: 接受邮箱
        subject: 邮件主题
        code: 验证码
    """
    html_content = f"您正在重设密码，验证码为：{code}, 5分钟内有效，请妥善保管"
    # send_email([to_mail], subject, html_content)