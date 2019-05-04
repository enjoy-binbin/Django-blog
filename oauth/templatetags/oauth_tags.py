from django import template
from django.urls import reverse

from oauth.manager import get_oauth_apps

register = template.Library()


@register.inclusion_tag('oauth/tag/oauth_apps.html')
def inclusion_oauth_apps(request):
    apps = get_oauth_apps()

    if apps:
        # 如果有oauth认证的app, 拼接字段返回给模板
        base_url = reverse('oauth:oauth_login')
        path = request.get_full_path()
        url = '{0}?type={1}'
        apps = map(lambda app: (app.NAME, url.format(base_url, app.NAME)), apps)

    return {
        'apps': apps
    }
