from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from pagedown.widgets import AdminPagedownWidget

from blog.forms import ArticleAdminForm
from blog.models import Article, Link, Setting


class ArticleAuthorListFilter(SimpleListFilter):
    """ 自定义查询的过滤器-根据文章作者过滤文章 """
    parameter_name = 'author_id'  # url中的参数名称
    title = '作者 (自定义的过滤器)'  # 右侧过滤器的title名称

    def lookups(self, request, model_admin):
        """ Must be overridden to return a list of tuples (value, verbose value) """
        # lambda article: article.author  # 接受一个article，返回对应作者对象
        # map(func, iterable)  # 将可迭代对象的每个元素传入func
        # author_list 所有文章的作者列表，去重
        author_list = list(set(map(lambda article: article.author, Article.objects.all())))

        # author_list2 = []
        # for author in author_list:
        #     author_list2.append((author.id, author.nickname or author.username))
        # return author_list2

        for author in author_list:  # verbose value, 在过滤器里显示的名称
            yield (author.id, (author.nickname or author.username))

    def queryset(self, request, queryset):
        """ Return the filtered queryset. """
        # 返回文章queryset里面 所有指定作者的文章
        author_id = self.value()
        if author_id:
            return queryset.filter(author__id=author_id)
        else:
            return queryset


# def add_article_order(modeladmin, request, queryset):
#     """ 列表页可执行的动作, 给所选文章的排序权重 加一
#     action写法: https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/
#     """
#     for article in queryset:
#         article.order += 1
#         article.save(update_fields=['order'])
#
#
# add_article_order.short_description = '给所选文章的排序权重 加一'


class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 100  # 每页显示几条数据
    list_display = ('id', 'title', 'author', 'category_link', 'views', 'order', 'status')  # 列表显示的字段
    list_display_links = ('id', 'title')  # 列表页可以跳转到详情页的字段
    # list_editable = ('views', 'order')  # 列表页可以编辑的字段
    search_fields = ('title', 'content')  # 搜索框可搜索的字段
    list_filter = ('category', ArticleAuthorListFilter, 'tags')  # 过滤器
    filter_horizontal = ('tags',)  # 编辑页多对多关系选择框，默认的不好用, 用这个或filter_vertical
    date_hierarchy = 'add_time'  # 按日期月份筛选
    ordering = ('order',)  # 排序的字段
    # actions = (add_article_order, )  # 列表页可执行的动作, 例如选中后执行删除
    actions = ('add_article_order', 'render_detail_html')  # 列表页可执行的动作, 例如选中后执行删除
    exclude = ('modify_time',)  # 详情页剔除的字段
    save_on_top = True  # 编辑页上也显示保存删除等按钮
    save_as = True  # 已有文章编辑页上 保存为新的

    # formfield_overrides = {models.TextField: {'widget': AdminPagedownWidget}, }  # way1
    form = ArticleAdminForm  # 给文章内容 content字段添加django-pagedown 编辑器 way2

    def category_link(self, obj):
        """ 链接到文章所属分类, obj是一个文章对象 """
        # 读一下 admin.urls的源码, admin的urlpatterns都是用get_urls实现的
        app_label = obj.category._meta.app_label  # app名称：blog
        model_name = obj.category._meta.model_name  # model名称：category

        # 比如说，分类详情页面，接收一个category_id
        # <URLPattern '<path:object_id>/change/' [name='blog_category_change']>
        # url为: /admin/blog/category/id/change
        # 对应为 reverse('admin:blog_category_change')
        link = reverse('admin:%s_%s_change' % (app_label, model_name), kwargs={'object_id': obj.category_id})
        return format_html(u'<a href="%s">%s</a>' % (link, obj.category))

    category_link.short_description = '文章所属分类'

    def get_form(self, request, obj=None, change=False, **kwargs):
        """ 文章详情页内选择作者, 只有超级管理员才会被filter出来
            Return a Form class for use in the admin add view.
        """
        form = super().get_form(request, obj=None, change=False, **kwargs)
        author_queryset = form.base_fields['author'].queryset
        if not request.user.is_superuser:
            # 不是超级管理员, 作者栏就只显示自己, 用于多用户
            form.base_fields['author'].queryset = author_queryset.filter(username=request.user.username)
            form.base_fields['order'].disabled = True  # 不允许修改排序和浏览量
            form.base_fields['views'].disabled = True
            # choices选择类型是一个list [(),()], 这里可以remove掉, 但是只剩下一个元素会出异常, 会需要try捕获, 表单是正常的
            # form.base_fields['type'].choices = form.base_fields['type'].choices.remove(('p', '页面'))
            form.base_fields['type'].disabled = True  # 这里也直接禁用掉吧, 根据默认值选
        else:
            form.base_fields['author'].queryset = author_queryset.filter(is_superuser=True)
        return form

    def get_queryset(self, request):
        """ 根据权限划分用户可以获取到的queryset """
        queryset = self.model._default_manager.get_queryset(hide=False)
        ordering = self.get_ordering(request)
        queryset = queryset.order_by(*ordering) if ordering else queryset

        if not request.user.is_superuser:
            self.list_filter = ()  # 普通用户取消过滤器
            return queryset.filter(author=request.user)
        else:
            return queryset

    def add_article_order(self, request, queryset):
        """ 列表页可执行的动作, 给所选文章的排序权重 加一
        action写法: https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/
        """
        success = list()
        for article in queryset:
            article.order += 1
            article.save(update_fields=['order'])
            success.append(article.title)

        self.message_user(request, f"{success} action successfully.")

    add_article_order.short_description = '给所选文章的排序权重 加一'

    def render_detail_html(self, request, queryset):
        """ 创建文章html """
        from utils.github_page import HtmlRender

        blog_setting = Setting.objects.all().first()
        success, error = [], []
        error_info = []

        for article in queryset:
            result, info = HtmlRender().detail(blog_setting, article)
            _ = success.append(article.title) if result else (error.append(article) or error_info.append(info))

        message = ''
        if success:
            message += f'{success} successfully'
        if error_info:
            message += f'{error} unsuccessfully, {error_info}'

        self.message_user(request, message)

    render_detail_html.short_description = '给所选的文章创建HTML静态文件'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'order')
    exclude = ('add_time', 'modify_time', 'slug')
    ordering = ('-order', '-parent_category')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_article_count')
    exclude = ('add_time', 'modify_time')


class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', 'is_enable')
    list_display_links = ('name', 'url')
    exclude = ('add_time', 'modify_time')


class SideBarAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': AdminPagedownWidget}, }
    exclude = ('add_time', 'modify_time')
    list_display = ('title', 'is_enable', 'order')
    list_editable = ('is_enable',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_link', 'content', 'parent_comment', 'is_enable')
    list_display_links = ('content',)
    search_fields = ('author', 'content', 'parent_comment')

    def author_link(self, obj):
        """ 链接到评论的作者, obj是一个评论对象 """
        app_label = obj.author._meta.app_label
        model_name = obj.author._meta.model_name

        link = reverse('admin:%s_%s_change' % (app_label, model_name), kwargs={'object_id': obj.author.id})
        return format_html('<a href="%s">%s</a>' % (link, obj.author))

    author_link.short_description = '评论者'


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'image', 'add_time')
    exclude = ('add_time', 'modify_time')


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('author_link', 'content', 'add_time')
    list_display_links = ('content',)

    def author_link(self, obj):
        """ 链接到评论的作者, obj是一个评论对象 """
        app_label = obj.author._meta.app_label
        model_name = obj.author._meta.model_name

        link = reverse('admin:%s_%s_change' % (app_label, model_name), kwargs={'object_id': obj.author.id})
        return format_html('<a href="%s">%s</a>' % (link, obj.author))

    author_link.short_description = '留言者'


class SettingAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'enable_photo', 'user_verify_email', 'enable_multi_user',
        'article_desc_len', 'sidebar_article_count'
    )
    list_editable = ('enable_photo', 'user_verify_email', 'enable_multi_user')
    save_on_top = True
    actions = ('render_index_html',)

    def has_add_permission(self, request):
        """ 唯一的站点配置, 不允许添加, 默认站点配置是在utils.get_setting里添加的 """
        return False

    def has_delete_permission(self, request, obj=None):
        """ 唯一的站点配置, 不允许删除 """
        return False

    def render_index_html(self, request, queryset):
        """ 创建博客首页index_html """
        from functools import partial
        from utils.github_page import HtmlRender

        blog_setting = queryset[0]
        article_list = Article.objects.all().order_by('-add_time')
        link_list = Link.objects.filter(is_enable=True).all()

        result, info = HtmlRender().index(blog_setting, article_list, link_list)

        message_user = partial(self.message_user, request=request, message=info)
        message_user(level=20) if result else message_user(level=40)

    render_index_html.short_description = '更新首页并且同步github-page'
