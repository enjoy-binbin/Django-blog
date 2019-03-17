2019年2月8日 18:37:25

	markdown越来越流行, 在博客网站上集成markdown

### 在admin后台编辑详情页里，给博客文章content加上markdown

查看我那篇关于admin设置的笔记文章吧。



### markdown你的博文

新建一个py文件，在后面用于引入。我是放在 utils目录下的

```python
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


# The fastest markdown parser in pure Python with renderer features, inspired by marked.
# https://github.com/lepture/mistune

class ArticleRenderer(mistune.Renderer):
    """ 对文章进行 markdown显示，和 代码高亮 """

    def block_code(self, code, lang=None):
        """Rendering block level code. ``pre > code``.

        :param code: text content of the code block.
        :param lang: language of the given code.
        """
        code = code.rstrip('\n')  # 去掉尾部的换行符
        if not lang:
            code = mistune.escape(code)
            return '<pre><code>%s\n</code></pre>\n' % code

        # 给代码加上高亮  例如: lang='python'的话
        # ```python
        #   print('666')
        # ```
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


def article_markdown(text):
    """ 对传入的text文本进行markdown """
    renderer = ArticleRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(text)

```



在blog_tags.py里自定义一个过滤器，在模板文件里对文章进行markdown

```python
from django.template.defaultfilters import stringfilter
from django import template

from utils.mistune_markdown import article_markdown as _article_markdown

register = template.Library()  # 名字是固定的register

@register.filter(is_safe=True)
@stringfilter
def article_markdown(text):
    """ 给文章加上 markdown支持 和 代码高亮 """
    return mark_safe(_article_markdown(text))
```



模板文件里面调用方式:   ( truncatechars_html过滤器是 django自带的可以用来截取html)

在列表页就截取部分长度的内容，而在文章详情页就不用截取

```
{{ article.content|article_markdown|truncatechars_html:250 }}
```