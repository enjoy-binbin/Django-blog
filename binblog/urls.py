from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from .admin import admin_site
from .sitemaps import StaticViewSitemap, ArticleSitemap, CategorySitemap, TagSitemap, AuthorSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'article': ArticleSitemap,
    'category': CategorySitemap,
    'tag': TagSitemap,
    'author': AuthorSitemap,
}

urlpatterns = [
    path('admin/', admin_site.urls),

    path('', include('blog.urls')),

    # path('', include('django.contrib.auth.urls')),  # 可以一读
    path('', include('user.urls')),

    path('search', include('haystack.urls')),  # django-haystack全局搜索

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps})  # sitemap

]

# 官网中的使用 GenericSitemap的例子
# from django.contrib.sitemaps import GenericSitemap
# from blog.models import Article

# info_dict = {
#     'queryset': Article.objects.all(),
#     'date_field': 'add_time',
# }
# path('sitemap.xml', sitemap,
#          {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
#          name='django.contrib.sitemaps.views.sitemap'),
