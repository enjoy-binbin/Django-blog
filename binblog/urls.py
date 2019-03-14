from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.conf import settings

from rest_framework_jwt.views import obtain_jwt_token

from .admin import admin_site
from .sitemaps import StaticViewSitemap, ArticleSitemap, CategorySitemap, TagSitemap, AuthorSitemap
from .feeds import BinBlogFeed

sitemaps = {
    'static': StaticViewSitemap,
    'article': ArticleSitemap,
    'category': CategorySitemap,
    'tag': TagSitemap,
    'author': AuthorSitemap,
}

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin_site.urls),

    path('', include('blog.urls', namespace='blog')),

    path('api-auth/', include('rest_framework.urls')),
    path('api/blog/', include('blog.api.urls', namespace='api-blog')),
    path('api/user/', include('user.api.urls', namespace='api-user')),
    path('api/auth/token/', obtain_jwt_token),

    path('', include('user.urls', namespace='user')),
    # path('', include('django.contrib.auth.urls')),  # 可以一读

    path('search', include('haystack.urls')),  # django-haystack全局搜索

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),  # sitemap

    path('feed/', BinBlogFeed(), name='feed'),
]

handler403 = 'blog.views.permission_denied'
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'
