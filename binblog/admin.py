from django.contrib.admin import AdminSite
from django.contrib.sites.models import Site
from django.contrib.sites.admin import SiteAdmin

from blog.models import (
    Setting,
    Category,
    Article,
    Comment,
    Tag,
    Link,
    SideBar,
    Photo,
    GuestBook,
)
from blog.admin import (
    ArticleAdmin,
    CategoryAdmin,
    TagAdmin,
    LinkAdmin,
    SideBarAdmin,
    SettingAdmin,
    CommentAdmin,
    PhotoAdmin,
    GuestBookAdmin,
)
from user.models import UserProfile
from user.admin import UserProfileAdmin
from oauth.models import OAuthConfig, OAuthUser
from oauth.admin import OAuthConfigAdmin


class BinBlogAdminSite(AdminSite):
    site_header = 'GMJ 博客后台管理'
    site_title = 'GMJ 博客后台管理'

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

admin_site.register(Site, SiteAdmin)  # 站点, sitemap使用
admin_site.register(Article, ArticleAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Tag, TagAdmin)
admin_site.register(Link, LinkAdmin)
admin_site.register(SideBar, SideBarAdmin)
admin_site.register(Setting, SettingAdmin)
admin_site.register(UserProfile, UserProfileAdmin)
admin_site.register(Comment, CommentAdmin)
admin_site.register(Photo, PhotoAdmin)
admin_site.register(GuestBook, GuestBookAdmin)

# admin_site.register(OAuthConfig, OAuthConfigAdmin)
