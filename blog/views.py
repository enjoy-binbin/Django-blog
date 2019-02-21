from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from blog.models import Article, Category, Tag, Comment
from blog.forms import CommentForm


class IndexView(ListView):
    """ 首页view，返回一些文章列表 """
    model = Article  # 指定的model
    template_name = 'blog/index.html'  # 渲染的模板
    context_object_name = 'article_list'  # 在模板中使用的上下文变量，默认为 object_list

    def get_queryset(self):
        queryset = super().get_queryset()  # 调用父类的方法
        # qs会根据model里定义的 ordering排序
        return queryset


class ArticleDetailView(DetailView):
    """ 文章详情页 """
    template_name = 'blog/article_detail.html'
    pk_url_kwarg = 'article_id'  # url里的id参数, 查找id为 pk_url_kwarg的文章
    model = Article
    context_object_name = 'article'
    object = None

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

    def get_queryset(self):
        slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=slug)
        all_category_name = list(map(lambda c: c.name, category.get_sub_categorys()))
        queryset = Article.objects.filter(category__name__in=all_category_name)
        return queryset


class TagArticleView(ListView):
    """ 获取一个标签下所有引用之的文章 """
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        tag_id = self.kwargs['tag_id']
        tag = get_object_or_404(Tag, id=tag_id)
        queryset = Article.objects.filter(tags=tag)
        return queryset


class AuthorArticleView(ListView):
    """ 获取一个作者下的所有文章列表 """
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        author_name = self.kwargs['author_name']
        queryset = Article.objects.filter(author__username=author_name)
        return queryset


class ArchivesView(ListView):
    """ 文章日期归档, queryset要有序的 """
    template_name = 'blog/archives.html'
    context_object_name = 'article_list'
    queryset = Article.objects.all().order_by('-add_time')


class CommentPostView(FormView):
    """
    A view that displays a form.
    On error, redisplays the form with validation errors;
    on success, redirects to a new URL.
    """
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
