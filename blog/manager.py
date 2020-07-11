from django.db.models import Manager


class TopCategoryManager(Manager):
    """ Django.Manager的用法，定义管理器，返回一级分类 """

    def get_queryset(self):
        return super().get_queryset().filter(parent_category=None)


class ArticleManager(Manager):
    def get_queryset(self, hide=True):
        """
        重写get_queryset方法, 默认不筛选隐藏状态下的文章, hide参数可以用来在admin中控制行为
        :param hide:    bool 如果为True, 则不显示隐藏的文章, 反之则显示
        :return:
        """
        queryset = super().get_queryset()
        queryset = queryset.exclude(status="hide") if hide else queryset
        return queryset
