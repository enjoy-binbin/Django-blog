# 使用django-haystack进行搜索, 引擎为 whoosh
# pip install django-haystack==2.8.1
# pip install pip install whoosh==2.7.4
# settings设置, 添加app, 和设置HAYSTACK_CONNECTIONS
# 使用haystack进行文章搜索(setting.py)
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'utils.whoosh_cn_backend.WhooshEngine',  # 自定义使用jieba进行中文分词
#         'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#     },
# }
# 自动更新搜索索引(setting.py)
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# 文档：https://django-haystack.readthedocs.io/en/v2.4.1/tutorial.html
# haystack只对在安装完毕后，重新添加的有效，之前创建的数据是没有建立索引无法搜索出来的(测试了好久/捂脸)
# 重建索引 ./manage.py rebuild_index
# 更新索引 ./manage.py update_index

from haystack import indexes

from blog.models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
