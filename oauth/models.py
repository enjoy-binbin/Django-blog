from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.core.exceptions import ValidationError

'''
{"login": "enjoy-binbin", "id": 22811481, "node_id": "MDQ6VXNlcjIyODExNDgx",
 "avatar_url": "https://avatars1.githubusercontent.com/u/22811481?v=4", "gravatar_id": "",
 "url": "https://api.github.com/users/enjoy-binbin", "html_url": "https://github.com/enjoy-binbin",
 "followers_url": "https://api.github.com/users/enjoy-binbin/followers",
 "following_url": "https://api.github.com/users/enjoy-binbin/following{/other_user}",
 "gists_url": "https://api.github.com/users/enjoy-binbin/gists{/gist_id}",
 "starred_url": "https://api.github.com/users/enjoy-binbin/starred{/owner}{/repo}",
 "subscriptions_url": "https://api.github.com/users/enjoy-binbin/subscriptions",
 "organizations_url": "https://api.github.com/users/enjoy-binbin/orgs",
 "repos_url": "https://api.github.com/users/enjoy-binbin/repos",
 "events_url": "https://api.github.com/users/enjoy-binbin/events{/privacy}",
 "received_events_url": "https://api.github.com/users/enjoy-binbin/received_events", "type": "User",
 "site_admin": false, "name": "Binbin Zhu", "company": null, "blog": "http://13.58.211.105/",
 "location": "China Guangzhou", "email": "binloveplay1314@qq.com", "hireable": null,
 "bio": "Web developer. Life is short, use python", "public_repos": 12, "public_gists": 0, "followers": 2,
 "following": 0, "created_at": "2016-10-13T08:37:22Z", "updated_at": "2019-05-02T07:13:35Z", "private_gists": 0,
 "total_private_repos": 1, "owned_private_repos": 1, "disk_usage": 211423, "collaborators": 0,
 "two_factor_authentication": false,
 "plan": {"name": "free", "space": 976562499, "collaborators": 0, "private_repos": 10000}}
'''


class OAuthUser(models.Model):
    """ 通过OAuth注册的用户 """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', blank=True, null=True,
                             on_delete=models.CASCADE)

    type = models.CharField('类型', max_length=50)
    nickname = models.CharField('昵称', max_length=50)
    email = models.CharField('邮箱', max_length=50, blank=True, null=True)
    avatar_url = models.CharField('头像链接', max_length=350, blank=True, null=True)
    user_info = models.TextField('OAuth获取的用户信息', blank=True, null=True)

    openid = models.CharField('用户openid', max_length=50)

    add_time = models.DateTimeField('添加时间', default=now)
    modify_time = models.DateTimeField('修改时间', default=now)

    class Meta:
        verbose_name = 'oauth用户'
        verbose_name_plural = verbose_name
        ordering = ['-add_time']

    def __str__(self):
        return self.nickname


class OAuthConfig(models.Model):
    type = models.CharField('OAuth类型', max_length=10)

    app_key = models.CharField('AppKey', max_length=200)
    app_secret = models.CharField('APPSecret', max_length=200)

    callback_url = models.CharField('回调地址', max_length=200, default='',
                                    help_text='http://127.0.0.1:8000/oauth/authorize?type=github')
    is_enable = models.BooleanField('是否启用', default=False)

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
