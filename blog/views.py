import logging

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.core.cache import cache
from django.urls import reverse
from django.contrib import messages

from blog.models import Article, Category, Tag, Comment, Photo, GuestBook
from blog.forms import CommentForm, GuestBookForm
from blog.tasks import test_add

# 日志器, 一般都用__name__作为日志器的名字, 在本例中日志器名称为 blog.views
# 一般如果直接使用 logging.error(msg), 日志器名称是为 root
logger = logging.getLogger(__name__)


class IndexView(ListView):
    """ 首页view，返回一些文章列表，TODO关于文章列表的展示，可以再抽象一个Base类 """
    model = Article  # 指定的model
    template_name = 'blog/index.html'  # 渲染的模板
    context_object_name = 'article_list'  # 在模板中使用的上下文变量，默认为 object_list
    page_kwarg = 'page'  # 前端约定好的页码的key

    def get_queryset(self):
        test_add.delay(5, 5)  # celery测试, 里面有睡了5秒, 但是异步体验不到, 看celery控制台的输出

        queryset = cache.get(self.cache_key)  # 查询缓存
        if not queryset:  # 缓存没命中会返回 None
            queryset = super().get_queryset()  # 调用父类的方法
            cache.set(self.cache_key, queryset)  # 设置缓存
        # qs会根据model里定义的 ordering排序
        return queryset

    # def get_queryset(self):
    #     queryset = super().get_queryset()  # 调用父类的方法
    #     # qs会根据model里定义的 ordering排序
    #     return queryset

    @property
    def page_value(self):
        """ 前端页码值，用于做缓存key的拼接 """
        page = self.request.GET.get(self.page_kwarg) or 1
        return page

    @property
    def cache_key(self):
        """ 缓存里的key """
        return 'index_%s' % self.page_value


class ArticleDetailView(DetailView):
    """ 文章详情页 """
    template_name = 'blog/article_detail.html'
    pk_url_kwarg = 'article_id'  # url里的id参数, 查找id为 pk_url_kwarg的文章
    model = Article
    context_object_name = 'article'
    object = None  # 当前文章对象, 感觉可以用property

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.add_views()  # 文章阅读量加一
        self.object = obj
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prev_article'] = self.object.prev_article
        context['next_article'] = self.object.next_article

        comment_form = CommentForm()
        user = self.request.user

        if user.is_authenticated:
            comment_form.fields['email'].initial = user.email  # 直接设置initial->value, 前端中这两个字段是hidden的
            comment_form.fields["name"].initial = user.username

        article_comments = self.object.get_comment_list()

        context['comment_form'] = comment_form
        context['article_comments'] = article_comments
        context['comment_count'] = len(article_comments) if article_comments else 0

        return context


class CategoryArticleView(ListView):
    """ 获取一个分类下的所有文章 """
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    object_name = None  # 当前分类对象
    page_kwarg = 'page'

    def get_queryset(self):
        queryset = cache.get(self.cache_key)
        if not queryset:
            slug = self.kwargs['slug']
            category = get_object_or_404(Category, slug=slug)
            self.object_name = category.name
            all_category_name = list(map(lambda c: c.name, category.get_sub_categorys()))
            queryset = Article.objects.filter(category__name__in=all_category_name)

            cache.set(self.cache_key, queryset)
        return queryset

    @property
    def page_value(self):
        page = self.request.GET.get(self.page_kwarg) or 1
        return page

    @property
    def cache_key(self):
        return '%s_%s' % (self.kwargs['slug'], self.page_value)


class TagArticleView(ListView):
    """ 获取一个标签下所有引用之的文章 """
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    page_kwarg = 'page'

    def get_queryset(self):
        queryset = cache.get(self.cache_key)
        if not queryset:
            tag_id = self.kwargs['tag_id']
            tag = get_object_or_404(Tag, id=tag_id)
            queryset = Article.objects.filter(tags=tag)

            cache.set(self.cache_key, queryset)
        return queryset

    @property
    def page_value(self):
        page = self.request.GET.get(self.page_kwarg) or 1
        return page

    @property
    def cache_key(self):
        return '%s_%s' % (self.kwargs['tag_name'], self.page_value)


class AuthorArticleView(ListView):
    """ 获取一个作者下的所有文章列表 """
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    page_kwarg = 'page'

    def get_queryset(self):
        queryset = cache.get(self.cache_key)
        if not queryset:
            author_name = self.kwargs['author_name']
            queryset = Article.objects.filter(author__username=author_name)
            cache.set(self.cache_key, queryset)
        return queryset

    @property
    def page_value(self):
        page = self.request.GET.get(self.page_kwarg) or 1
        return page

    @property
    def cache_key(self):
        return '%s_%s' % (self.kwargs['author_name'], self.page_value)


class ArchivesView(ListView):
    """ 文章日期归档, 归档的话queryset是要有序的 """
    template_name = 'blog/archives.html'
    context_object_name = 'article_list'
    queryset = Article.objects.all().order_by('-add_time')


class PhotoListView(ListView):
    """ 相册列表 -> 这个的模板相对来说没下面的好看 """
    model = Photo
    template_name = 'blog/photo.html'
    context_object_name = 'photo_list'


class PhotoListView2(ListView):
    """ 相册2列表-> 这个的模板有bug: 模态框弹出有多一个滚动条 """
    model = Photo
    template_name = 'blog/photo2.html'
    context_object_name = 'photo_list'


class GuestBookListView(ListView):
    """ 站点留言板列表 """
    template_name = 'blog/guestbook.html'
    context_object_name = 'guestbook_list'
    queryset = GuestBook.objects.all().order_by('-add_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        guestbook_form = GuestBookForm()
        context['guestbook_form'] = guestbook_form

        return context


class GuestBookPostView(FormView):
    """ 提交留言 """
    form_class = GuestBookForm
    template_name = 'blog/guestbook.html'

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('blog:guestbook'))

    def form_valid(self, form):
        """ post提交的数据通过表单验证后 """
        guestbook = form.save(False)
        guestbook.author = self.request.user

        guestbook.save(True)
        messages.success(self.request, '留言成功')
        return HttpResponseRedirect(reverse('blog:guestbook'))


class CommentPostView(FormView):
    """ 评论post提交的VIew """
    form_class = CommentForm
    template_name = 'blog/article_detail.html'

    def get(self, request, *args, **kwargs):
        # get直接请求url的话就跳到文章底部的评论框
        article_id = kwargs['article_id']
        article = get_object_or_404(Article, id=article_id)

        url = article.get_absolute_url()
        return HttpResponseRedirect(url + "#comments")

    def form_valid(self, form):
        """ post提交的数据通过表单验证后 """

        article_id = self.kwargs['article_id']

        article = get_object_or_404(Article, id=article_id)

        comment = form.save(False)
        comment.article = article
        comment.author = self.request.user

        if form.cleaned_data['parent_comment_id']:
            # 如果有父评论
            parent_comment = Comment.objects.get(id=form.cleaned_data['parent_comment_id'])
            comment.parent_comment = parent_comment

        comment.save(True)
        return HttpResponseRedirect("%s#div-comment-%d" % (article.get_absolute_url(), comment.id))

    def form_invalid(self, form):
        # 未通过表单验证
        # 只有登陆的用户才可以发评论，且在form中, 把部分字段设置成hidden了
        # 所以这个的触发概率很小
        article_id = self.kwargs['article_id']
        article = get_object_or_404(Article, id=article_id)

        if self.request.user.is_authenticated:
            user = self.request.user
            form.fields["email"].initial = user.email
            form.fields["name"].initial = user.username

        return self.render_to_response({
            'form': form,
            'article': article
        })


# 403的抛出
# from django.core.exceptions import PermissionDenied
# raise PermissionDenied
def permission_denied(request, exception, template_name='blog/error_page.html'):
    """ 处理403错误码 """
    logger.error(exception)
    error_msg = '403错误拉，没有权限访问当前页面，点击首页看看别的？'
    return render(request, template_name, {
        'error_msg': error_msg,
    }, status=403)


def page_not_found(request, exception, template_name='blog/error_page.html'):
    """ 处理404错误码 """
    if exception:  # 记录下404的错误地址
        logger.error({'status': '404', 'path': exception.args[0]['path']})  # 中文链接不会被url encode

    url = request.get_full_path()  # 这个url如果带有中文会被 url encode
    error_msg = '404错误啦，访问的地址 ' + url + ' 不存在。请点击首页看看别的？'
    return render(request, template_name, {
        'error_msg': error_msg,
    }, status=404)


def server_error(request, template_name='blog/error_page.html'):
    """ 处理500错误码 """
    error_msg = '500错误啦，服务器出错，我已经收集到了错误信息，之后会抓紧抢修，请点击首页看看别的？'
    return render(request, template_name, {
        'error_msg': error_msg,
    }, status=500)
