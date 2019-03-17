### Django中的ContentType模型

文档地址：https://docs.djangoproject.com/en/2.1/ref/contrib/contenttypes/



参考文章：

https://www.cnblogs.com/lddhbu/archive/2012/07/18/2597755.html

https://www.cnblogs.com/c491873412/p/7892585.html

django中对contenttype的应用

首先在instaled_apps中可以看到 `'django.contrib.contenttypes',`

数据库表中也有`django_content_type`这张表，表结构数据大致如下，存储着app_label和model的关系

| id   | app_label | model   |
| ---- | --------- | ------- |
| 1    | blog      | article |
| 2    | blog      | movie   |
| 3    | blog      | comment |



下面代码使用场景：

有 文章，电影等模型类， 有一个 评论类，给文章 or 电影 or 其他以后出现的（音乐、游戏）的评论

当评论表，要增加列比如 文章、电影表的外键字段 article_id，movie_id建立外键关系时，就可以使用

```python
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class Movie(models.Model):
   title = models.CharField(max_length=100)
   comment = GenericRelation('Comment')  # GenericRelation不会生成额外的列

class Article(models.Model):
   title = models.CharField(max_length=100)
   comment = GenericRelation('Comment')

class Comment(models.Model):
   content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # 外键
   object_id = models.IntegerField()  # 对应的那个对象的id
   content_object = GenericForeignKey()  # 对应的那个对象，不会生成额外的列
   title = models.CharField(max_length=100)
```

先看Comment。Comment中使用 `GenericForeignKey()` 来指向其它的Model实例。为了使用它，你还需要在Model中定义  `content_type` 和 `object_id` 才可以。其中content_type是指向`ContentType`这个Model。

在Django中，你如何定位一条记录？一般需要三个值：`app_label` ,  `model` 和  `object_id`。

在`django_content_type`表中就是保存了`app_label`和`model`的关系。因此使用`GenericForeignKey`你就只要两个值了。但`content_object`本身还是要定义一下的，不会生成`content_object`c这个列。默认情况下是GenericForeignKey("content_type","object_id")，你也可以自定义那些字段的名称，但是还是默认最好，

结果还是三项。使用其实还是挺简单的。看文档就ok。



创建上面的模型后，进入django shell进行操作，体验一下。

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py shell

>>> from content.models import *
>>> article = Article(title='i am a article')
>>> article.save()
>>> article.id  # 在文章表内的的文章id
6
>>>
>>> movie = Movie(title='i am a movie')  # movie同样可以和执行和article相同的操作
>>> movie.save()
>>>
>>> article_comment = Comment()
>>> article_comment.content_object = article  # 这里只需指定 content_object
>>> article_comment.title = 'this article is really nice'
>>> article_comment.save()

>>> article_comment.title
>>> 'this article is really nice'
>>> article_comment.content_type
>>> <ContentType: article>
>>> article_comment.content_object
>>> <Article: Article object (6)>
>>> article_comment.object_id  # 
>>> 6

>>> article.comment.all()  # 可以根据GenericRelation这样取得所有的comments
<QuerySet [<Comment: Comment object (6)>]>
```

