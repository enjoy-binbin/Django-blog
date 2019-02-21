from django.contrib.admin import AdminSite


class BinBlogAdminSite(AdminSite):
    site_header = 'BinBlog 后台管理'
    site_title = 'BinBlog 后台管理'

    def __init__(self, name='admin'):
        """ AdminSite追进去看 """
        super().__init__(name)

    def has_permission(self, request):
        """ 重载登陆后台权限设置
        Return True if the given HttpRequest has permission to view
        """
        # return request.user.is_active and request.user.is_staff
        return request.user.is_superuser


admin_site = BinBlogAdminSite(name='admin')
