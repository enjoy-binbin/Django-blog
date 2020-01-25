import random

from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.timezone import now

from blog.models import Article, Category, Link, SideBar, Tag, Comment
from utils.get_setting import get_setting
from utils.mistune_markdown import article_markdown as _article_markdown

register = template.Library()  # 名字是固定的register
setting = get_setting()


@register.inclusion_tag('blog/tags/article_info.html', takes_context=True)
def inclusion_article_info_tag(context, article, is_index):
    """
    在首页index和 文章详情页detail里使用，用于加载文章info
    is_index 是否首页列表页, 首页加载只显示摘要
    inclusion_tag里好像无法获取到 模板全局变量
    """
    return {
        'article': article,
        'user': context['user'],
        'is_index': is_index,
        'ARTICLE_DESC_LEN': setting.article_desc_len  # 文章摘要长度, 用于index页面
    }


# 如果是一个安全的字符串经过过滤，结果还是安全的
# is_save为True的作用, 不安全的通过过滤, 会将其转义
# return truncatechars_html('<br>'+text, 300)
# 上面例子里 +了 <br> 会被判断整个text 是不安全的
# 设置为Ture后,就会对text进行转义
@register.filter(is_safe=True)
@stringfilter
def article_markdown(text):
    """ 给文章加上 markdown支持 和 代码高亮 """
    return mark_safe(_article_markdown(text))


@register.simple_tag
def queryset_filter_tag(queryset, **kwargs):
    """ template tag which allows queryset filtering. Usage:
          {% filter_tag books author=author as mybooks %}
          {% for book in mybooks %}
          {% endfor %}
    """
    return queryset.filter(**kwargs)


@register.inclusion_tag('blog/tags/sidebar.html', takes_context=True)
def inclusion_sidebar_tag(context):
    """ 引入站点右侧侧边栏 """
    count = setting.sidebar_article_count  # 站点设置中侧边栏显示记录条数

    # 相关上下文变量设置
    all_articles = Article.objects.only('title', 'views', 'add_time')  # only只查这些字段
    hot_articles = all_articles.order_by('-views')[:count]  # 最热文章
    new_articles = all_articles.order_by('-add_time')[:count]  # 最新文章
    all_categories = Category.objects.all()  # 全部分类
    all_sidebars = SideBar.objects.filter(is_enable=True).order_by('-order')  # 侧边栏
    all_links = Link.objects.filter(is_enable=True)  # 友情链接
    all_comments = Comment.objects.filter(is_enable=True).order_by('-add_time')[:count]  # 新的评论

    # 标签云，根据标签被引用的次数，增大标签的字体大小
    # 算法: 单个标签字体大小 = 单个标签出现次数 / 所有标签被引用的总次数 / 标签个数 * 增长幅度 + 最小字体大小
    all_tags = Tag.objects.all()  # 全部标签
    if all_tags:
        # lambda 传入一个Tag对象, 返回 tag_ref_list = [(Tag, 标签被引用的次数)]
        tag_ref_list = list(map(lambda t: (t, t.get_article_count()), all_tags))
        tag_ref_count = sum(map(lambda t: t[1], tag_ref_list))  # 所有标签被引用的总次数

        increment = 4  # 增长幅度
        min_pt = 10  # 最小字体大小 10pt, 单个标签被引用次数为0的话, 字体大小为 0+min_pt
        # 标签被引用的总次数 / 标签总数, 当文章总引用数为0时, 将fre置为1
        frequency = (tag_ref_count / len(all_tags)) or 1

        # tag,count,size
        all_tags = list(map(lambda x: (x[0], x[1], (x[1] / frequency) * increment + min_pt), tag_ref_list))
        random.shuffle(all_tags)  # 将标签再随机排序

    return {
        'hot_articles': hot_articles,
        'new_articles': new_articles,
        'all_categories': all_categories,
        'all_sidebars': all_sidebars,
        'all_links': all_links,
        'all_tags': all_tags,
        'all_comments': all_comments,
        'user': context['user'],  # inclusion_tag的模板里好像接受不到 request全局对象

        'github_sidebar': '%s/%s' % (setting.github_user, setting.github_repository)
    }


@register.filter()
def time_filter(time):
    """ 自定义时间过滤器 """
    # timestamp为间隔时间, 这里需要注意 time和now有 是否包办时区之分的格式
    # 设置setting.USE_TZ为False 或者 去除时间里的 now=now.replace(tzinfo=None)
    timestamp = (now() - time).total_seconds()

    if timestamp < 60:
        return '刚刚呀'
    elif (timestamp >= 60) and (timestamp < 60 * 60):
        minute = int(timestamp / 60)
        return '%s 分钟前' % minute
    elif (timestamp >= 60 * 60) and (timestamp < 60 * 60 * 24):
        hour = int(timestamp / 60 / 60)
        return '%s 小时前' % hour
    elif (timestamp >= 60 * 60 * 24) and (timestamp < 60 * 60 * 24 * 30):
        day = int(timestamp / 60 / 60 / 24)
        return '%s 天前' % day
    else:
        return time.strftime('%Y/%m/%d %H:%M')


@register.simple_tag(takes_context=True)
def pagination_tag(context, object_list, page_count=5):
    """ context是Context 对象，object_list是你要分页的对象，page_count表示每页的数量 """
    paginator = Paginator(object_list, page_count)
    page = context['request'].GET.get('page')  # 前端里规定的字段, 传来的页码page

    try:
        object_list = paginator.page(page)  # 根据页码获取对应页的数据

    except PageNotAnInteger:
        # 如果page不是int，字符串或为None，就返回第一页
        object_list = paginator.page(1)

    except EmptyPage:
        # 如果page是int, 负数，或0，或者超过最大页数，返回最后一页
        object_list = paginator.page(paginator.num_pages)

    return object_list  # 模板里as可以取得return {% pagination_tag article_list 2 as article_list %}


@register.inclusion_tag('blog/tags/comment_item.html')
def inclusion_comment_item(comment):
    """ 一个个评论item """
    return {
        'comment': comment
    }


@register.simple_tag()
def parse_comment_tree(comment_list, comment):
    """ 获得当前评论子评论的列表 """
    # comment_list 所有评论， comment当前评论
    # {% parse_comment_tree article_comments comment as childcomments %}
    child_comments = []

    def parse(parent_comment):
        child_comment_list = comment_list.filter(parent_comment=parent_comment, is_enable=True)
        for child_comment in child_comment_list:
            child_comments.append(child_comment)
            parse(child_comment)

    parse(comment)
    return child_comments


@register.inclusion_tag('blog/tags/breadcrumb.html')
def inclusion_breadcrumb_tag(article):
    """ 获得文章分类树, 用作面包屑导航 """
    category_tree = article.get_category_tree()  # [(分类, 分类url), (父类, 父类url)]
    category_tree.append((setting.name, '/'))  # 将首页append进去
    category_tree.reverse()  # 列表倒序 或者切片list[::-1]

    return {
        'category_tree': category_tree,
        'title': article.title
    }


@register.inclusion_tag('blog/tags/article_meta_info.html', takes_context=True)
def inclusion_article_meta_tag(context, article):
    """ 获得文章meta信息, 发布时间和作者 """
    return {
        'article': article,
        'user': context['user'],  # 文章作者可以直接跳转到后台管理页
    }
