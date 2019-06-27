import requests
from urllib import parse

from .models import OAuthConfig, OAuthUser


class BaseManager(object):
    """ 基类, 封装一些方法, 这里可以写成抽象类接口的 """
    NAME = None

    def get_config(self):
        """ 获取指定type的配置信息 """
        config = OAuthConfig.objects.filter(type=self.NAME)
        return config[0] if config else None


class GitHubOauthManager(BaseManager):
    """ github oauth登陆 """
    # https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/
    NAME = 'github'
    AUTH_URL = 'https://github.com/login/oauth/authorize'  # get方法获取code
    TOKEN_URL = 'https://github.com/login/oauth/access_token'  # post方法获取token
    API_URL = 'https://api.github.com/user'  # 获取用户信息

    def __init__(self):
        config = self.get_config()
        self.client_id = config.app_key if config else ''
        self.client_secret = config.app_secret if config else ''
        self.callback_url = config.callback_url if config else ''  # 需要和github里设置的一致

    def get_authorization_url(self, nexturl='/'):
        """ 获得用户授权, 通过后会向redirect_uri发送get请求, 并携带着一个临时的code参数 """
        params = {
            'client_id': self.client_id,  # github中注册的client_id
            'redirect_uri': self.callback_url + '&next_url=' + nexturl,  # 认证后的回调函数
            # scope 授予权限的说明 https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/
            'scope': '(no scope)',
            # 'state': 'bin_bin',  # 不可猜测的随机字符串, 用来防止CSRF的, 非必需
            'allow_signup': 'true',  # 提供一个注册github的入口
        }
        url = self.AUTH_URL + "?" + parse.urlencode(params)
        return url

    def get_access_token_by_code(self, code, state='bin_bin'):
        """ 根据上一步授权通过的code交换access_token, 如果有定义state, 就可以在这里判断是否第三方 """
        params = {
            'client_id': self.client_id,  # github中注册的client_id
            'client_secret': self.client_secret,  # github中注册的client_secret
            'code': code,  # 上一步授权通过的临时code
            # 'redirect_uri': self.callback_url,  # 回调地址, 非必需
            # 'state': 'bin_bin',  # 不可猜测的随机字符串, 用来防止CSRF的, 非必需
        }

        # 'access_token=0b9a86333da97bb4ccc46dae36c200281710a00a&scope=&token_type=bearer'
        text = requests.post(self.TOKEN_URL, params).text
        res = parse.parse_qs(text)  # 会返回字典, 如果没得parse, 返回空字典
        return res['access_token'][0] if res else None

    def get_oauth_user(self, access_token):
        """ 根据上一步的access_token, 获取用户信息, 返回oauth_user """
        params = {'access_token': access_token}

        res = requests.get(self.API_URL, params).json()

        oauth_user = OAuthUser()
        oauth_user.type = 'github'
        oauth_user.openid = res.get('id', '')
        oauth_user.nickname = res.get('name', '')
        oauth_user.avatar_url = res.get('avatar_url', '')
        oauth_user.email = res.get('email', '')
        oauth_user.user_info = res  # 将整个返回结果写入

        # 不进行保存, 直接返回, 还需判断该oauth_user是否存在
        return oauth_user


def get_oauth_apps():
    configs = OAuthConfig.objects.filter(is_enable=True).all()
    if not configs:
        return []
    configtypes = [x.type for x in configs]
    applications = BaseManager.__subclasses__()
    apps = [x() for x in applications if x().NAME.lower() in configtypes]
    return apps


def get_manager_by_type(type):
    if not type:
        return None
    applications = get_oauth_apps()
    if applications:
        finds = list(filter(lambda x: x.NAME.lower() == type.lower(), applications))
        if finds:
            return finds[0]
    return None
