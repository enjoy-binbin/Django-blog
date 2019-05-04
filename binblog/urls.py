from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.conf import settings

from rest_framework_jwt.views import obtain_jwt_token

from user.views import refresh_cache
from .admin import admin_site
from . import sitemaps
from .feeds import BinBlogFeed

sitemaps = {
    'static': sitemaps.StaticViewSitemap,
    'article': sitemaps.ArticleSitemap,
    'category': sitemaps.CategorySitemap,
    'tag': sitemaps.TagSitemap,
    'author': sitemaps.AuthorSitemap,
}

urlpatterns = [
    # admin后台管理
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin_site.urls),

    # md编辑器, 对比与pagedown有在线上传图片的功能
    path('mdeditor/', include('mdeditor.urls')),

    path('', include('oauth.urls', namespace='oauth')),
    path('', include('blog.urls', namespace='blog')),
    path('', include('user.urls', namespace='user')),
    # django自带登陆注册等方法的可以读
    # path('', include('django.contrib.auth.urls')),

    # Djangorestframework  rest-api的学习
    path('api-auth/', include('rest_framework.urls')),
    path('api/blog/', include('blog.api.urls', namespace='api-blog')),
    path('api/user/', include('user.api.urls', namespace='api-user')),
    path('api/auth/token/', obtain_jwt_token),

    # django-haystack全局搜索, 站点地图, feed订阅, 超级管理员刷新缓存
    path('search', include('haystack.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('feed/', BinBlogFeed(), name='feed'),
    path('refresh/', refresh_cache, name='refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 全局403 404 500设置
handler403 = 'blog.views.permission_denied'
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'
