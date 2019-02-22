# 使用django的标签和Paginator进行文章分页

2019年2月15日 09:08:16

```python
# blog_tags.py 标签文件中

from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
register = template.Library()  # 名字是固定的register

@register.simple_tag(takes_context=True)
def pagination_tag(context, object_list, page_count=2):
    """ context是Context 对象，object_list是你要分页的对象，page_count表示每页的数量 """
    paginator = Paginator(object_list, page_count)
    page = context['request'].GET.get('page')

    try:
        object_list = paginator.page(page)  # 根据页码获取对应页的数据

    except PageNotAnInteger:
        # 如果page不是int，字符串或为None，就返回第一页
        object_list = paginator.page(1)

    except EmptyPage:
        # 如果page是int, 负数，或0，或者超过最大页数，返回最后一页
        object_list = paginator.page(paginator.num_pages)
        
	# 模板里as可以取得return {% pagination_tag article_list 2 as article_list %}
    return object_list  
```

```python
# 模板文件中对views中传来的 article_list 进行标签调用，进行分页
{% pagination_tag article_list 2 as article_list %}

{% for article in article_list %}
    {% inclusion_article_info_tag article True %}
{% endfor %}

{% include 'blog/article_pagination.html' %}
```

``` html
<nav id="nav-below" class="navigation" role="navigation">
    {% if article_list.has_previous %}
        <div class="nav-previous"><a href="?page={{ article_list.previous_page_number }}">
            <span class="meta-nav">←</span>上一页</a>
        </div>
    {% endif %}
    {% if article_list.has_next %}
        <div class="nav-next"><a href="?page={{ article_list.next_page_number }}">
            <span class="meta-nav">→</span>下一页</a>
        </div>
    {% endif %}
</nav>
```