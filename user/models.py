from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.urls import reverse


class UserProfile(AbstractUser):
    """ 自定义 User模型扩充字段，需要继承AbstractUser """
    GENDER_CHOICE = (
        ('male', '男'),
        ('female', '女')
    )

    nickname = models.CharField('昵称', max_length=30, blank=True)
    gender = models.CharField('性别', max_length=6, choices=GENDER_CHOICE, default='male')
    add_time = models.DateTimeField('添加时间', default=now)
    modify_time = models.DateTimeField('修改时间', default=now)

    # USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('blog:author_article', kwargs={
            'author_name': self.username
        })


class EmailVerifyCode(models.Model):
    """ 邮箱验证码 """
    TYPE_CHOICE = (
        ('register', '注册'), ('forget', '忘记密码'), ('change', '修改邮箱')
    )

    code = models.CharField('验证码', max_length=20)
    email = models.EmailField('邮箱', max_length=50)
    type = models.CharField('类型', max_length=20, choices=TYPE_CHOICE)
    is_used = models.BooleanField('是否激活', default=False)
    add_time = models.DateTimeField('发送时间', default=now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
