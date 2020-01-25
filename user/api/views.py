from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView,
)
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer
)

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    """ 用户创建API """
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    """ 用户登陆API """
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)

        # 当设置了 raise_exception=True 会自动 抛出ValidationError(errors)和return 400
        # return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
