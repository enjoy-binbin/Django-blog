记录一下

    class CustomBackend(ModelBackend):
        """
            settings里配置AUTHENTICATION_BACKENDS
            这里将email和username和nickname都当作username进行Q并起来
        """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(nickname=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None



settings里
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)