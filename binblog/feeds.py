from django.contrib.syndication.views import Feed

from blog.models import Article


class BinBlogFeed(Feed):
    title = '彬彬博客'  # xml里的 title, link, desc标签内容
    link = '/feed/'
    description = '彬彬博客Feed'

    def items(self):
        """ returns a list of objects that should be included in the feed as <item> elements. """
        return Article.objects.order_by('-add_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return item.get_absolute_url()

    def item_author_name(self, item):
        return item.author.username

    def feed_copyright(self):
        return 'Copyright (c) 2019, Zhu Binbin'
