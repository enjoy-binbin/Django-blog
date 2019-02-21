from django.db import models
from django.utils.timezone import now  # 跟根据USE_TZ的值返回带时区或不带时区的datetime
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.template.defaultfilters import slugify

from unidecode import unidecode


class Setting(models.Model):
    """ 全局站点设置常量 """
    name = models.CharField('站点名称', max_length=100, default='')
    desc = models.TextField('站点描述', default='')
    keyword = models.TextField('站点关键字', default='')
    article_desc_len = models.IntegerField('文章摘要长度', default=250)
    sidebar_article_count = models.IntegerField('侧边栏文章条数', default=10)

    github_user = models.CharField('github账号', max_length=50, default='')
    github_repository = models.CharField('github仓库', max_length=50, default='')

    class Meta:
        verbose_name = '站点配置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def clean(self):
        """
        在admin创建或者修改一个实例时，会调用这个方法。而model.save()不会调用
        """
        if Setting.objects.exclude(id=self.id):
            raise ValidationError(_('只能有一个配置'))


class BaseModel(models.Model):
    """
        自定义的BaseModel抽象类，增加多几个字段
        抽象类不会对应数据库表
    """
    id = models.AutoField(primary_key=True)
    add_time = models.DateTimeField("添加时间", default=now)
    modify_time = models.DateTimeField("修改时间", default=now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.modify_time = now()
        super().save(*args, **kwargs)


class Article(BaseModel):
    """ 文章模型 """
    category = models.ForeignKey('Category', verbose_name='文章分类', on_delete=models.CASCADE)
    title = models.CharField('文章标题', max_length=100, unique=True)
    content = models.TextField('文章内容')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    order = models.IntegerField('排序,越大越前', default=0)
    views = models.PositiveIntegerField('浏览量', default=0)
    tags = models.ManyToManyField('Tag', verbose_name='标签', blank=True)
    pub_time = models.DateTimeField('发布时间', blank=True, null=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-order', '-pub_time', '-add_time']
        # get_latest_by = 'id'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={
            'article_id': self.id,
            'title': self.title
        })

    def add_views(self):
        """ 文章浏览量自增 """
        self.views += 1
        self.save(update_fields=['views'])

    def next_article(self):
        """ 下一篇的文章 """
        return Article.objects.filter(id__gt=self.id).order_by('id').first()

    def prev_article(self):
        """ 上一篇的文章 """
        return Article.objects.filter(id__lt=self.id).first()

    def get_comment_list(self):
        """ 获取当前文章下的评论列表 """
        comment_list = self.comment_set.filter(is_enable=True)
        return comment_list


class Category(BaseModel):
    """ 文章分类 """
    name = models.CharField('分类名称', max_length=30, unique=True)
    parent_category = models.ForeignKey('self', verbose_name='父级分类', blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, default='')

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category_article', kwargs={
            'slug': self.slug
        })

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def get_parent_categorys(self):
        """ 递归获取分类的父级分类 """
        categorys = []

        def parse(category):
            categorys.append(category)
            if category.parent_category:
                parse(category.parent_category)

        parse(self)
        return categorys

    def get_sub_categorys(self):
        """ 获取当前分类下的所有子分类 """
        categorys = []
        all_categorys = Category.objects.all()

        def parse(category):
            if category not in categorys:
                categorys.append(category)
            sub_categorys = all_categorys.filter(parent_category=category)
            for sub_category in sub_categorys:
                parse(sub_category)

        parse(self)
        return categorys


class Tag(BaseModel):
    """ 文章标签 """
    name = models.CharField('标签名', max_length=25, unique=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag_article', kwargs={
            'tag_id': self.id,
            'name': self.name
        })

    def get_article_count(self):
        """ 获取单个标签引用下的所有文章数量 """
        return Article.objects.filter(tags__name=self.name).count()


class Link(BaseModel):
    """ 友情链接 """
    name = models.CharField('链接名称', max_length=30, unique=True)
    order = models.IntegerField('排序,越大越前', default=0)
    url = models.URLField('链接地址')
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.name


class SideBar(BaseModel):
    """ 站点右上角的侧边栏，可以显示一些html,markdown内容 """
    title = models.CharField('标题', max_length=30)
    content = models.TextField('内容')
    order = models.IntegerField('排序,越大越前', default=1)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        ordering = ['-order']
        verbose_name = '侧边栏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='评论者', on_delete=models.CASCADE)
    content = models.TextField('评论内容', max_length=250)
    article = models.ForeignKey(Article, verbose_name='评论文章', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', verbose_name='父评论', blank=True, null=True, on_delete=models.CASCADE)
    is_enable = models.BooleanField('是否显示', default=True)

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author
