from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.contrib.auth import login

from oauth.manager import get_manager_by_type
from oauth.models import OAuthUser

User = get_user_model()


class OAuthLoginView(View):
    """ OAuth登陆View, 返回OAuth app的认证页 """

    def get(self, request):
        type = request.GET.get('type', None)
        if not type:
            return HttpResponseRedirect('/')
        manager = get_manager_by_type(type)
        if not manager:
            return HttpResponseRedirect('/')

        # 首先进来, 需要获取 code
        url = manager.get_authorization_url()
        return HttpResponseRedirect(url)


class OAuthAuthorize(View):
    """ OAuth认证 """

    def get(self, request):
        _type = request.GET.get('type', None)  # oauth_app类型
        code = request.GET.get('code', None)  # 授权码

        manager = get_manager_by_type(_type)
        if not manager:
            return HttpResponseRedirect('/')

        access_token = manager.get_access_token_by_code(code)
        if not access_token:  # code过期, 或者信息不正确, token没拿到
            return HttpResponseRedirect(reverse('user:login'))

        oauth_user = manager.get_oauth_user(access_token)  # 返回的是个OAuthUser对象

        try:  # 这里其实也可以用get_or_create
            # 根据openid检查该oauth用户是否存在, 存在就更新下表字段信息
            _oauth_user = OAuthUser.objects.get(type=_type, openid=oauth_user.openid)
            _oauth_user.nickname = oauth_user.nickname
            _oauth_user.email = oauth_user.email
            _oauth_user.avatar_url = oauth_user.avatar_url
            _oauth_user.user_info = oauth_user.user_info
            _oauth_user.save()
            oauth_user = _oauth_user
            del _oauth_user
        except ObjectDoesNotExist:
            pass

        # 根据外键查找oauth用户是否有关联的user用户
        users = User.objects.filter(id=oauth_user.user_id)
        user = users[0] if users else None

        # oauth用户有email的话就根据email关联到user_model表
        if oauth_user.email:
            if not user:
                # 第一次oauth, 没有和oauth_user相对应的user_model
                # 就用邮箱create后用外键关联起来
                # 之后再访问就都用get获取, 或者关联已有的user用户
                res = User.objects.get_or_create(email=oauth_user.email)  # 返回(obj, bool)
                user = res[0]  # get到或者create的obj对象,

                # 如果是create就为True, get到的就为False
                if res[1]:
                    # 如果是create得到的user, 说明是第一次oauth
                    user.username = oauth_user.nickname
                    user.nickname = oauth_user.nickname
                    user.save()
                else:
                    # 是get的到的, 说明里面原本就有个相同邮箱的user, 就不进行操作
                    # 就有可能是多个相同邮箱的oauth_app进行登陆
                    pass

                oauth_user.user = user
                oauth_user.save()

            login(request, user)
            return HttpResponseRedirect('/')

        # oauth_user里没有邮箱信息的话, 就需要验证邮箱
        # 还没遇到过就先 TODO吧, 思路就是 传入oauth_user的id, 在另外个视图里判断吧
        else:
            # oauth_user.save()
            if not user:  # oauth_user.user_id == None
                pass
            else:
                pass
