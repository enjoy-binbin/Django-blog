from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.timezone import now  # 跟根据USE_TZ的值返回带时区或不带时区的datetime
from django.utils.translation import gettext_lazy as _
from mdeditor.fields import MDTextField
from unidecode import unidecode

from blog.manager import TopCategoryManager


class Setting(models.Model):
    """ 全局站点设置常量 """
    name = models.CharField(_('站点名称'), max_length=100)
    desc = models.TextField(_('站点描述'), default='', blank=True)
    keyword = models.TextField(_('站点关键字'), default='', blank=True)
    article_desc_len = models.IntegerField(_('文章摘要长度'), default=250)
    sidebar_article_count = models.IntegerField(_('侧边栏文章条数'), default=10)
    enable_photo = models.BooleanField(_('是否启用相册'), default=True)
    user_verify_email = models.BooleanField(_('用户注册是否验证邮箱'), default=False)
    enable_multi_user = models.BooleanField(
        _('是否启用多用户博客系统'), default=False,
        help_text=_('是否启用多用户博客系统, 注册用户只具有对自己文章的增删改查权限')
    )
    github_avatar = models.CharField(
        _('github头像'), max_length=50, default='https://avatars2.githubusercontent.com/u/22811481',
        help_text='https://avatars2.githubusercontent.com/u/22811481'
    )
    github_user = models.CharField(
        _('github账号'), max_length=50, default='enjoy-binbin',
        help_text='https://github.com/enjoy-binbin'
    )
    github_repository = models.CharField(
        _('github仓库'), max_length=50, default='Django-blog',
        help_text='https://github.com/enjoy-binbin/Django-blog'
    )
    about_me = models.TextField(_('关于我'), default='Hello World', blank=True)

    class Meta:
        verbose_name = _('0-站点配置')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def clean(self):
        # 会先执行clean, 无论是否修改了数据都会执行
        # 会根据当前有几条记录执行几次(类似善后工作), self是一条条记录本身
        # 在admin创建或者修改一个实例时，会调用这个方法。而instance.save()不会调用
        if Setting.objects.exclude(id=self.id):
            raise ValidationError(_('只能有一个配置'))

    def save(self, *args, **kwargs):
        # clean后再执行save, 会根据当前修改了几条记录执行几次, self是一条条记录本身
        super().save(*args, **kwargs)


class BaseModel(models.Model):
    """
        自定义的BaseModel抽象类，增加多几个字段
        抽象类不会对应数据库表
    """
    id = models.AutoField(primary_key=True)  # django默认也是会加一个id作为主键的
    add_time = models.DateTimeField(_("添加时间"), default=now)
    modify_time = models.DateTimeField(_("修改时间"), default=now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # 在save之前修改下修改时间
        self.modify_time = now()
        super().save(*args, **kwargs)


class Category(BaseModel):
    """ 文章分类 """
    name = models.CharField(_('分类名称'), max_length=30, unique=True)
    parent_category = models.ForeignKey('self', verbose_name=_('父级分类'), blank=True, null=True, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(_('排序'), default=0, help_text=_('越大越前'))
    slug = models.SlugField(max_length=50, default='')

    objects = models.Manager()  # 当自定义了管理器，django将不再默认管理对象objects了, 需要手动指定
    top_objects = TopCategoryManager()  # 调用方式: Category.top_object.all()

    class Meta:
        verbose_name = _('1-文章分类')
        verbose_name_plural = verbose_name
        ordering = ['-order', 'add_time']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category_article', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def get_parent_categorys(self):
        """ 递归获取分类的父级分类 [自己, 父类1, 父类2] """
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


class Article(BaseModel):
    """ 文章模型 """
    TYPE_CHOICES = (
        ('a', _('文章')),  # 对应一篇篇文章
        ('p', _('页面')),  # 也是文章, 但是可以用于渲染当导航烂(例如 关于我)
    )

    category = models.ForeignKey('Category', verbose_name=_('文章分类'), on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('作者'), on_delete=models.CASCADE)
    title = models.CharField(_('文章标题'), max_length=100, unique=True)
    content = MDTextField(_('文章内容'))  # 使用了django-mdeditor作为md编辑器
    type = models.CharField(_('文章类型'), max_length=1, default='a', choices=TYPE_CHOICES)
    order = models.PositiveSmallIntegerField(_('排序'), default=0, help_text=_('越大越前'))
    views = models.PositiveIntegerField(_('浏览量'), default=0)
    tags = models.ManyToManyField('Tag', verbose_name=_('标签'), blank=True)

    class Meta:
        verbose_name = _('2-文章')
        verbose_name_plural = verbose_name
        ordering = ['-order', '-add_time']
        # get_latest_by = 'id'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={
            'article_id': self.id,
            'title': self.title
        })

    def get_github_page_url(self):
        return f'/{self.category}/{self.title}.html'

    def add_views(self):
        """ 文章浏览量自增 """
        # self.views = models.F('views') + 1  # 会变成: F(views) + Value(1), 得再取过
        # self.save()
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

    def get_category_tree(self):
        """ 获得当前文章的分类树, 用于详情页面包屑 """
        categorys = self.category.get_parent_categorys()  # [文章分类, 分类的父类1, ...]
        category_tree = list(map(lambda category: (category.name, category.get_absolute_url()), categorys))
        return category_tree

    def get_admin_url(self):
        """ 获取当前文章在admin里的详情页 """
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=(self.id,))


class Comment(BaseModel):
    """ 文章评论 """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('评论者'), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name=_('评论文章'), on_delete=models.CASCADE)
    content = models.TextField(_('评论内容'), max_length=250)
    parent_comment = models.ForeignKey('self', verbose_name=_('父评论'), blank=True, null=True, on_delete=models.CASCADE)
    is_enable = models.BooleanField(_('是否显示'), default=True)

    class Meta:
        verbose_name = _('3-文章评论')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Tag(BaseModel):
    """ 文章标签 """
    name = models.CharField(_('标签名'), max_length=25, unique=True)

    class Meta:
        verbose_name = _('4-文章标签')
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag_article', kwargs={
            'tag_id': self.id,
            'tag_name': self.name
        })

    def get_article_count(self):
        """ 获取单个标签引用下的所有文章数量 """
        return Article.objects.filter(tags__name=self.name).count()

    get_article_count.short_description = _('标签引用文章数')


class SideBar(BaseModel):
    """ 站点右上角的侧边栏，可以显示一些html,markdown内容 """
    title = models.CharField(_('标题'), max_length=30)
    content = models.TextField(_('内容'))
    order = models.PositiveSmallIntegerField(_('排序'), default=1, help_text=_('越大越前'))
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        verbose_name = _('5-侧边栏')
        verbose_name_plural = verbose_name
        ordering = ['-order']

    def __str__(self):
        return self.title


class Link(BaseModel):
    """ 友情链接 """
    name = models.CharField(_('链接名称'), max_length=30, unique=True)
    order = models.PositiveSmallIntegerField(_('排序'), default=0, help_text=_('越大越前'))
    url = models.URLField(_('链接地址'))
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        verbose_name = _('8-友情链接')
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.name


def photo_path(instance, filename):
    """ 根据图片标题和图片后缀, 拼接上传路径 """
    # idx = filename.rfind('.')
    # name = filename[:idx]  # 返回文件名的前缀
    # ext = filename[idx:]  # 返回文件名的后缀 .ext
    ext = filename.split('.')[-1]
    filename = 'photo/{}.{}'.format(instance.title, ext)
    return filename


class Photo(BaseModel):
    """ 相册照片 """
    title = models.CharField(_('图片标题'), max_length=50, help_text=_('用于当作照片名称'))
    desc = models.TextField(_('图片描述'), max_length=200, help_text=_('用于图片标签的title属性'), null=True, blank=True)
    image = models.ImageField(_('图片'), upload_to=photo_path, help_text=_('默认保存在/media/photo/'))

    class Meta:
        verbose_name = _('6-相册图片')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GuestBook(BaseModel):
    """ 留言板留言 """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('留言者'), on_delete=models.CASCADE)
    content = models.TextField(_('留言内容'), max_length=250)

    class Meta:
        verbose_name = _('7-留言板')
        verbose_name_plural = verbose_name
        ordering = ['author', '-id']

    def __str__(self):
        return '%s - %s' % (self.author, self.content)
