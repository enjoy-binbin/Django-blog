先简单介绍下RSS:

> RSS（简易信息聚合）是一种消息来源格式规范，用以聚合经常发布更新数据的网站，例如博客文章、新闻、音频或视频的网摘。RSS文件（或称做摘要、网络摘要、或频更新，提供到频道）包含全文或是节录的文字，再加上发布者所订阅之网摘数据和授权的元数据。

其实就是一种聚合阅读，这样可以用feedly等工具来订阅你喜欢的网站，这样他们的网站更新了之后你就可以通过feedly这种工具来阅读更新的内容，而不用跑到网站上面去查看。



﻿官方文档地址: https://docs.djangoproject.com/en/2.1/ref/contrib/syndication/

2019年2月25日 14:02:23

一个简单的RSS-feed功能

在binblog目录下(与settings平级)，创建feeds.py文件

```python
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
```

urls.py下的配置

```python
from .feeds import BinBlogFeed

urlpatterns = [
    ...
    path('feed/', BinBlogFeed()),
]
```

运行，浏览器打开127.0.0.1:8000/feed/，下载一段xml文本

打开里面就是了，里面有很多元素都是可以自定义的

参考文档: https://docs.djangoproject.com/en/2.1/ref/contrib/syndication/#feed-class-reference