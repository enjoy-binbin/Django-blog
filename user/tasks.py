import time
import hashlib

from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from celery import shared_task

from binblog.settings import EMAIL_FROM  # setting文件设置的发件人

logger = get_task_logger(__name__)


@shared_task
def send_email_task(email, code_str, send_type):
    """
    使用celery异步发送邮件
    @email 邮件收件方
    @code_str 邮件验证码
    @send_type: 邮件类型
    """
    if send_type == 'register':
        subject = '彬彬博客注册激活链接'
        message = '请点击下面的链接激活您的账号: http://127.0.0.1:8000/active/{0}'.format(code_str)

    elif send_type == 'forget':
        subject = '彬彬博客忘记密码连接'
        timestamp = int(time.time())
        md5 = hashlib.md5()
        md5_str = md5.update((code_str + email + str(timestamp)).encode('utf8'))
        hash_str = md5.hexdigest()
        message = '请点击下面的链接修改你的密码: http://127.0.0.1:8000/reset?timestamp={0}&hash={1}&email={2}'.format(timestamp,
                                                                                                        hash_str, email)
    elif send_type == 'change':
        subject = '彬彬博客修改邮箱连接'
        message = '你的邮箱验证码为: {0}'.format(code_str)
    else:
        logger.error('非法的发送类型'.format(email))
        return {'status': 'fail', 'error': 'illegal send_type'}

    status = send_mail(subject, message, EMAIL_FROM, [email])  # ,html_message=

    if status:
        logger.info('{0}邮件发送成功'.format(email))
        return {'status': 'success', 'email': email}
    else:
        logger.error('{0}邮件发送失败'.format(email))
        return {'status': 'fail', 'email': email}
