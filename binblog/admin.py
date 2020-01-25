from django.contrib.admin import AdminSite
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site

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
from oauth.admin import OAuthConfigAdmin
from oauth.models import OAuthConfig
from user.admin import UserProfileAdmin, EmailVerifyCodeAdmin, LogEntryAdmin
from user.models import UserProfile, EmailVerifyCode
from utils.get_setting import get_setting


class BinBlogAdminSite(AdminSite):
    site_header = '彬彬博客后台管理'
    site_title = '彬彬博客后台管理'

    def __init__(self, name='admin'):
        """ AdminSite追进去看 """
        super().__init__(name)

    def has_permission(self, request):
        """ 重载登陆后台权限设置
        Return True if the given HttpRequest has permission to view
        """
        s = get_setting()
        if s.enable_multi_user:
            # 启动了多用户管理系统, 用户具有staff权限可以登陆后台
            return request.user.is_active and request.user.is_staff
        else:
            # 否则只有超级管理员有权限登陆后台
            return request.user.is_superuser


admin_site = BinBlogAdminSite(name='admin')

admin_site.register(Setting, SettingAdmin)  # 站点配置

admin_site.register(Category, CategoryAdmin)  # 文章分类
admin_site.register(Article, ArticleAdmin)  # 文章
admin_site.register(Comment, CommentAdmin)  # 文章评论
admin_site.register(Tag, TagAdmin)  # 文章标签
admin_site.register(SideBar, SideBarAdmin)  # 侧边栏
admin_site.register(Photo, PhotoAdmin)  # 相册
admin_site.register(GuestBook, GuestBookAdmin)  # 留言板
admin_site.register(Link, LinkAdmin)  # 友情链接

admin_site.register(UserProfile, UserProfileAdmin)  # 用户
admin_site.register(EmailVerifyCode, EmailVerifyCodeAdmin)  # 邮箱验证码

admin_site.register(OAuthConfig, OAuthConfigAdmin)  # OAuth设置

admin_site.register(Site, SiteAdmin)  # 站点, sitemap使用
admin_site.register(Group, GroupAdmin)  # 用户组, 管理权限
admin_site.register(Permission)  # 权限
admin_site.register(LogEntry, LogEntryAdmin)  # 日志管理
