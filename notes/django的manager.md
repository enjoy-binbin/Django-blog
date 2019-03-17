### Django的managers

文档地址：https://docs.djangoproject.com/en/2.1/topics/db/managers/



Article.objects.all()    objects就是一个manager管理器，django会默认给所有模型增添上objects管理器

下面是创建自定义manager的两个原因： 增加额外的manager方法，或修改manager返回的初始QuerySet。

增加额外的manager方法可以将经常使用的查询进行封装，就不用重复编码了



#### 修改manager返回的初始QuerySet简单用法：

场景：在博客中，找出所有的一级分类

当然，我们可以 Category.objects.filter(parent_category=None)

或者，用管理器 Category.top_objects.all()



```python
class TopCategoryManager(models.Manager):
    """ Django.Manager的用法，定义管理器，返回一级分类 """

    def get_queryset(self):
        return super().get_queryset().filter(parent_category=None)

class Category(BaseModel):
    """ 文章分类 """
    name = models.CharField('分类名称', max_length=30, unique=True)
    parent_category = models.ForeignKey('self', verbose_name='父级分类', blank=True, null=True, on_delete=models.CASCADE)

    objects = models.Manager()  # 当自定义了管理器，django将不再默认管理对象objects了, 需要手动指定
    top_objects = TopCategoryManager()  # 调用方式: Category.top_object.all()
```

