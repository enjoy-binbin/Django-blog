# 使用django-haystack进行搜索, 引擎为 whoosh
# pip install django-haystack==2.8.1
# pip install pip install whoosh==2.7.4
# settings设置, 添加app, 和设置HAYSTACK_CONNECTIONS
# 文档：https://django-haystack.readthedocs.io/en/v2.4.1/tutorial.html
# haystack只对在安装完毕后，重新添加的有效，之前创建的数据是没有建立索引无法搜索出来的(测试了好久/捂脸)

from haystack import indexes
from blog.models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
