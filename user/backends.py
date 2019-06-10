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
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            # User.set_password(password)
            pass
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                # 通过密码验证
                return user

    def user_can_authenticate(self, user):
        """ 重载了这个方法, 达到django.contrib.auth.backends.AllowAllUsersModelBackend一样的效果
            跟 AllowAllUsersModelBackend 一样的效果, 但 is_active为False为False, 会报未激活
            ModelBackend原先的user_can_authenticate方法, 但is_active为False, 会报账号不存在
            即 请输入一个正确的 用户名 和密码. 注意他们都是大区分大小写的.
        """
        return True
