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

    def __str__(self):
        return '%s -- %s' % (self.username, self.email)

    def get_absolute_url(self):
        return reverse('blog:author_article', kwargs={
            'author_name': self.username
        })
