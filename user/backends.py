from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginByUsernameOrEmailBackend(ModelBackend):
    """
        这里将email和username都当作username进行Q并起来, 可以根据邮箱或者用户名登陆
        settings里配置 AUTHENTICATION_BACKENDS = ('user.backends.LoginByUsernameOrEmailBackend',)
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                # 通过密码验证
                return user
        except User.DoesNotExist:
            return None
