### 为django的manage添加命令

文档地址：https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/

2019年2月26日 10:38:31

在已注册的app目录下 创建 `management目录`和，接着在在management目录下创建`commands目录`和`__init__.py文件`，最后在`commands目录`下创`建命令py文件`和`__init__.py`，文件名即为命令

django/core/management/commands/...  (django的命令源码)

下面创建一个命令create_testdata，执行命令后会向表里插入一些博客测试数据

```powershell
# 目录结构为
├─management
│  │  __init__.py
│  │
│  └─commands
│          create_testdata.py
│          __init__.py
```



create_testdata.py文件

~~~python
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from blog.models import Article, Tag, Category

user_model = get_user_model()


class Command(BaseCommand):
    """ run manage.py create_testdata """
    help = 'create test datas'

    def handle(self, *args, **options):
        # get_or_create 没有便创建, 返回一个元组 (obj, created)
        user = user_model.objects.get_or_create(
            username='testadmin', password='abc123456.0', email='test@qq.com',
            is_staff=True, is_superuser=True)[0]

        parent_category = Category.objects.get_or_create(name='python学习', parent_category=None)[0]

        sub_category = Category.objects.get_or_create(name='django学习', parent_category=parent_category)[0]

        basetag = Tag.objects.get_or_create(name='Django')[0]

        # 创建20篇测试文章
        for i in range(1, 20):
            article = Article.objects.get_or_create(
                category=sub_category,
                title='我是测试标题 ' + str(i),
                content='我是测试内容 ' + str(i),
                author=user
            )[0]
            tag = Tag.objects.get_or_create(name='标签' + str(i))[0]

            article.tags.add(tag)
            article.tags.add(basetag)
            article.save()

        # 创建文章
        article = Article.objects.get_or_create(
            category=sub_category,
            title='彬彬博客',
            content="""### 支持Markdown

```python
print('支持语法高亮')
```
            """,
            author=user
        )[0]
        article.tags.add(basetag)
        article.save()

        self.stdout.write(self.style.SUCCESS('Data created sucessfully！ \n'))
~~~

之后在命令行里运行

```
python manage.py create_testdata
```

