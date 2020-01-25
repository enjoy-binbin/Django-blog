from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _  # 懒翻译, 国际化


class UserProfile(AbstractUser):
    """ 自定义 User模型扩充字段，需要继承AbstractUser """
    GENDER_CHOICE = (
        ('male', _('男')),
        ('female', _('女'))
    )

    nickname = models.CharField(_('昵称'), max_length=30, blank=True)
    gender = models.CharField(_('性别'), max_length=6, choices=GENDER_CHOICE, default='male', blank=True)
    email = models.EmailField(_('邮箱地址'))
    # add_time = models.DateTimeField('_(添加时间)', default=now)  # 有个默认的date_joined可以用
    modify_time = models.DateTimeField(_('修改时间'), default=now)

    class Meta:
        verbose_name = _('0-用户')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.modify_time = now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:author_article', kwargs={'author_name': self.username})

    def user_level(self):
        """ 根据用户权限在admin里颜色化处理 """
        if self.is_superuser:
            color = 'green'
            content = _('超级管理员')
        elif self.is_staff:
            color = 'green'
            content = _('博客用户')
        elif self.is_active:
            color = 'black'
            content = _('注册用户')
        else:
            color = 'red'
            content = _('未激活用户')

        return format_html('<span style="color: {0}">{1}</span>', color, content)

    user_level.short_description = _('用户等级')


class EmailVerifyCode(models.Model):
    """ 邮箱验证码 """
    TYPE_CHOICE = (
        ('register', _('注册')), ('forget', _('忘记密码')), ('change', _('修改邮箱'))
    )

    code = models.CharField(_('验证码'), max_length=20)
    email = models.EmailField(_('邮箱'), max_length=50)
    type = models.CharField(_('类型'), max_length=20, choices=TYPE_CHOICE)
    task_id = models.CharField(_('任务的uuid'), max_length=36, blank=True, default='', help_text='celery.task_id')
    is_used = models.BooleanField(_('是否使用'), default=False)
    add_time = models.DateTimeField(_('发送时间'), auto_now_add=True)  # auto_now_add 第一次创建时设为当前时间, 且在admin只读
    modify_time = models.DateTimeField(_('更新时间'), auto_now=True)  # auto_now 适用于更新时间, 每次保存当前时间, admin只读

    class Meta:
        verbose_name = _('1-邮箱验证码')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

    def expired(self):
        if self.is_used:  # 如果用了
            return None

        timestamp = (now() - self.add_time).total_seconds()
        if timestamp > 10 * 60:  # 验证码10分钟过期
            color = 'red'
            content = _('已过期')
        else:
            color = 'green'
            content = _('未过期')

        return format_html('<span style="color: {0}">{1}</span>', color, content)

    expired.short_description = _('是否过期')
