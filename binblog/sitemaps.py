from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Article, Category, Tag


class StaticViewSitemap(Sitemap):
    """ 静态视图，例如抓取index页 """
    priority = 0.5  # 优先级
    changefreq = 'daily'  # 更改频率，文档里查找可使用的属性值

    def items(self):
        # 在items里显式列出静态视图名称
        return ['blog:index', ]

    def location(self, item):
        # 在location里用reverse调用, item是一个个items返回后的对象
        return reverse(item)


class ArticleSitemap(Sitemap):
    """ 指向所有文章条目链接的Sitemap """
    changefreq = 'daily'
    priority = 0.6

    def items(self):
        # 必需，返回一个对象列表，可以自己filter过滤, 被其他方法属性调用
        return Article.objects.all()

    def lastmod(self, obj):
        # 可选，返回个datetime类型，表示items返回的每个对象的最后修改时间
        return obj.modify_time

    def location(self, obj):
        # 可选，返回每个obj对象的绝对路径，默认会调用obj.get_absolute_url方法
        return reverse('blog:article_detail', kwargs={'article_id': obj.id, 'title': obj.title})


class CategorySitemap(Sitemap):
    """ 指向所有文章分类链接的Sitemap """
    changefreq = 'Weekly'
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.modify_time


class TagSitemap(Sitemap):
    """ 指向所有标签条目链接的Sitemap """
    changefreq = 'Weekly'
    priority = 0.4

    def items(self):
        return Tag.objects.all()

    def lastmod(self, obj):
        return obj.last_mod_time


class AuthorSitemap(Sitemap):
    """ 指向所有作者条目链接的Sitemap """
    changefreq = 'Weekly'
    priority = 0.3

    def items(self):
        return list(set(map(lambda article: article.author, Article.objects.all())))

    def lastmod(self, obj):
        return obj.date_joined
