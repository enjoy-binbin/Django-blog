from django.db.models import Manager


class TopCategoryManager(Manager):
    """ Django.Manager的用法，定义管理器，返回一级分类 """

    def get_queryset(self):
        return super().get_queryset().filter(parent_category=None)
