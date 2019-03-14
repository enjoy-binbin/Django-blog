from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
    ValidationError,
)

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    """ 创建用户序列化 """
    email = EmailField(label='邮箱地址')
    email2 = EmailField(label='验证邮箱')

    class Meta:
        model = User
        fields = ['username', 'email', 'email2', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        """ 会先等到validate_xxx验证通过才执行 """
        # email = attrs['email']
        # user_queryset = User.objects.filter(email=email)
        # if user_queryset.exists():  # 判断邮箱是否存在
        #     raise ValidationError('This user has already registered.')

        return attrs

    def validate_email2(self, value):
        """ 验证两个邮箱是否匹配 """
        data = self.get_initial()
        email = data.get('email')
        if email != value:
            raise ValidationError('Emails must match.')

        user_queryset = User.objects.filter(email=email)
        if user_queryset.exists():  # 判断邮箱是否存在
            raise ValidationError('This email has already registered.')

        return value

    def create(self, validated_data):
        """ 重载create方法, 创建用户 """
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    """ 用户登陆序列化 """
    token = CharField(read_only=True)
    username = CharField(label='用户名', required=False)
    email = EmailField(label='邮箱', required=False)

    class Meta:
        model = User
        fields = ['token', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        user_obj = None
        username = attrs.get('username', None)  # 因为不是必需的, 所以要get获取
        email = attrs.get('email', '')
        password = attrs['password']

        if not username and not email:
            raise ValidationError('A username or email must provide to login.')

        user_queryset = User.objects.filter(
            Q(username=username) |
            Q(email=email)
        ).exclude(email__iexact='')

        # 防止 username 和 email 各匹配出一个user
        # username在数据库层是唯一的, email是注册层唯一 (admin里可以设置相同的email)
        if user_queryset.exists() and user_queryset.count() == 1:
            user_obj = user_queryset.first()
        else:
            raise ValidationError('This username or email is not valid.')

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Wrong account or password please try agin.')

        attrs['token'] = '6666'

        return attrs
