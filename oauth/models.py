from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.core.exceptions import ValidationError


class OAuthUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', blank=True, null=True,
                             on_delete=models.CASCADE)

    nickname = models.CharField('昵称', max_length=50)
    type = models.CharField('类型', max_length=50)
    email = models.CharField('邮箱', max_length=50, blank=True, null=True)
    picture = models.CharField('头像', max_length=350, blank=True, null=True)
    matedate = models.CharField(max_length=3000, blank=True, null=True)

    openid = models.CharField('用户openid', max_length=50)
    token = models.CharField('token值', max_length=150, blank=True, null=True)

    add_time = models.DateTimeField('添加时间', default=now)
    modify_time = models.DateTimeField('修改时间', default=now)

    class Meta:
        verbose_name = 'oauth用户'
        verbose_name_plural = verbose_name
        ordering = ['-add_time']

    def __str__(self):
        return self.nickname


class OAuthConfig(models.Model):
    TYPE_CHOICE = (
        ('github', 'GitHub'),
        ('qq', 'QQ'),
        ('weibo', '微博'),
        ('google', '谷歌'),
        ('facebook', 'FaceBook'),
    )
    type = models.CharField('类型', max_length=10, choices=TYPE_CHOICE, default='a')

    appkey = models.CharField('AppKey', max_length=200)
    appsecret = models.CharField('APPSecret', max_length=200)
    callback_url = models.CharField('回调地址', max_length=200, default='')
    is_enable = models.BooleanField('是否启用', default=True)

    add_time = models.DateTimeField('添加时间', default=now)
    modify_time = models.DateTimeField('修改时间', default=now)

    class Meta:
        verbose_name = 'OAuth配置'
        verbose_name_plural = verbose_name
        ordering = ['-add_time']

    def __str__(self):
        return self.type

    def clean(self):
        if OAuthConfig.objects.filter(type=self.type).exclude(id=self.id):
            raise ValidationError(self.type + '已经存在')
