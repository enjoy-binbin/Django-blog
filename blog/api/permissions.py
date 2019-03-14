from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    """ Allow access only to superusers. """

    message = 'Allow access only to superusers.'

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff and
            request.user.is_superuser
        )


class IsAuthor(BasePermission):
    """ 检查登陆用户是否是 文章作者 """

    message = 'You must be the author of this article.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsAuthorOrReadOnly(BasePermission):
    """ 检查登陆用户是否是 文章作者 """
    safe_method = ['GET', 'PUT', 'DELETE', 'OPTIONS']
    message = 'You must be the author of this article.'

    # 会先判断has_permission，为True才会判断has_object_permission, 为False直接返回
    # 视图级判断，判断请求方式, GET, PUT, DELETE, OPTIONS
    # def has_permission(self, request, view):
    #     if request.method in self.safe_method:
    #         return True
    #
    #     self.message = 'This request method is not allow.'
    #     return False

    # 对象级判断，判断 是否有权限访问对象
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET',):  # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            # Check permissions for read-only request
            return True

        # Check permissions for write request
        # 对于其他通过的例如 put修改, delete删除 就判断是否 是作者
        return (request.user == obj.author) or request.user.is_superuser
