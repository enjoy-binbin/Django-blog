2019年2月07日 20:26:12

https://blog.csdn.net/weixin_42134789/article/details/80327619

1. 展示对象列表（比如所有用户，所有文章）- ListView

1. 展示某个对象的详细信息（比如用户资料，比如文章详情) - DetailView

1. 通过表单创建某个对象（比如创建用户，新建文章）- CreateView

1. 通过表单更新某个对象信息（比如修改密码，修改文字内容）- UpdateView

1. 用户填写表单后转到某个完成页面 - FormView

1. 删除某个对象 - DeleteView





###  ListView视图，get_queryset()方法
	ListView它完成的功能和 article_list = Article.objects.all() 这句代码类似，获取某个 指定Model 的列表（这里是文章列表），同时我们加入了自己的逻辑，只找出对应作者的文章列表，假如仅仅只需要获取 article_list ，则甚至可以不用复写 get_queryset 方法，只需指定一个 model 属性，告诉 Django 去获取哪个 model 的列表就可以了  ListView默认会返回指定Model.objects.all()
	
	# Create your views here.
	from django.views.generic import ListView
	from .models import Article
	 
	class IndexView(ListView):
	 
	    model = Article  # 指定的model，或者可以直接在 get_queryset里 model.object.all()
	    template_name = 'blog/article_list.html'  # 指定这个视图渲染的模板
		# 默认为object_list 在模板上下文使用的 {{ article_list }}
	    context_object_name = 'article_list'  
	 
	    def get_queryset(self):
	        qs = super().get_queryset() # 调用父类方法
	        return qs.filter(author = self.request.user).order_by('-pub_date')
	
	# 在url里需要捕获的参数调用
	从 URL 捕获的命名组参数值保存在实例的 kwargs 属性（是一个字典）里，非命名组参数值保存在实例的 args 属性（是一个列表）里。类似这样调用 id = self.kwargs.get('id') 




### get_context_data()
	get_context_data可以用于给模板传递模型以外的内容或参数，非常有用。例如现在的时间并不属于Article模型。如果你想把现在的时间传递给模板，你还可以通过重写get_context_data方法（如下图所示)。因为调用了父类的方法，
	
	# Create your views here.
	from django.views.generic import ListView
	from .models import Article
	from django.utils import timezone
	 
	class IndexView(ListView):
	 
	    queryset = Article.objects.all().order_by("-pub_date")  # 可以不写get_queryset方法
	    template_name = 'blog/article_list.html'
	    context_object_name = 'article_list'
	 
	    def get_context_data(self, **kwargs):
	        context = super().get_context_data(**kwargs)  # py3中可以直接super()调用父类的方法
	        context['now'] = timezone.now()  # 只有这行代码有用，在模板中调用 article_list['now']
	        return context  # 模板上下文中的变量


### DetailView视图的 get_object()方法
	DetailView和EditView都是从URL根据pk或其它参数调取一个对象来进行后续操作。下面代码通过DetailView展示一条记录数据的详细信息。get_object 方法默认情况下获取 id 为pk_url_kwarg 的对象
	
	from django.views.generic import DetailView
	from django.http import Http404
	from .models import Article
	from django.utils import timezone
	 
	class ArticleDetailView(DetailView):
	 
	    queryset = Article.objects.all().order_by("-pub_date")
	    template_name = 'blog/article_detail.html'
	    context_object_name = 'article'  # 默认为 object 
		pk_url_kwarg = 'article_id'  # 默认可以不写，自动调用 id=为pk_url_kwarg的对象
	 
		# 对于类似文章阅读量的增加，可以重写 DetailView的 get方法或者在 get_obejct方法里加
	    def get_object(self, queryset=None):
	        obj = super().get_object(queryset=queryset)
	        if obj.author != self.request.user:
	            raise Http404()
	        return obj


​			






Django模板标签regroup的妙用

    1 年，5 月前 3431 字 5991 阅读 22 评论 

在使用 Django 开发时，有时候我们需要在模板中按对象的某个属性分组显示一系列数据。例如博客文章按照时间归档分组显示文章列表（示例效果请看我的博客的归档页面），或者需要按日期分组显示通知（例如知乎）的通知列表。如果不熟悉 Django 内置的 regroup 模板标签，要完成这个需求可能还得费点功夫，而使用 regroup 则可以轻松完成任务。
regroup 官方文档示例

regroup 可以根据一个类列表对象中元素的某个属性对这些元素进行重新分组。例如有这样一个记录各个国家各个城市信息的列表：

cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
]

我们想按照国家分组显示各个国家的城市信息，效果就像这样：

    India
    Mumbai: 19,000,000
    Calcutta: 15,000,000
    USA
    New York: 20,000,000
    Chicago: 7,000,000
    Japan
    Tokyo: 33,000,000

在模板中使用 regroup 模板标签就可以根据 country 属性对 cities 进行分组：

{% regroup cities by country as country_list %}

<ul>
{% for country in country_list %}
    <li>{{ country.grouper }}
    <ul>
        {% for city in country.list %}
          <li>{{ city.name }}: {{ city.population }}</li>
        {% endfor %}
    </ul>
    </li>
{% endfor %}
</ul>

基本用法为 {% regroup 类列表对象 by 列表中元素的某个属性 as 模板变量 %}

例如示例中根据 cities 列表中元素的 country 属性 regroup 了 cities，并通过 as 将分组后的结果保存到了 country_list 模板变量中。

然后可以循环这个分组后的列表。被循环的元素包含两个属性：

    grouper，就是分组依据的属性值，例如这里的 ‘India’、‘Japan’
    list，属于该组下原列表中元素

博客文章按日期归档

官方的例子是分组一个列表，且列表的元素是一个字典。但 regroup 不仅仅限于分组这样的数据结构，只要是一个类列表对象都可以分组，例如一个 QuerySet 对象。举一个博客文章例子，假设博客文章的 Model 定义如下：

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DatetimeField() # 文章发布时间

现在要按照发布日期的年、月对文章进行分组显示，例如最开始给出的我的个人博客的归档页面示例，可以这样做：

{% regroup post_list by created_time.year as year_post_group %}

<ul>
  {% for year in year_post_group %}
  <li>{{ year.grouper }} 年
    {% regroup year.list by created_time.month as month_post_group %}
    <ul>
      {% for month in month_post_group %}
      <li>{{ month.grouper }} 月
        <ul>
          {% for post in month.list %}
          <li><a href="{{ post.get_absolute_url }}">{{ post.title }}</a>
          </li>
          {% endfor %}
        </ul>
      </li>
      {% endfor %}
    </ul>
  </li>
  {% endfor %}
</ul>

假设模板中有一个包含 Post 列表的变量 post_list，先按照年份对其分组，然后循环显示这些年份，而在某个年份的循环中，又对该年份下的文章按照月份对其分组，然后循环显示该年中各个月份下的文章，这样就达到了一个日期归档的效果。

只要分好组后，就可以任意控制模板显示的内容了，例如你不想循环显示全部文章标题，只想显示各个月份下的文章数量，稍微修改一下模板即可：

{% regroup post_list by created_time.year as year_post_group %}

<ul>
  {% for year in year_post_group %}
  <li>{{ year.grouper }} 年
    {% regroup year.list by created_time.month as month_post_group %}
    <ul>
      {% for month in month_post_group %}
      <li>{{ month.grouper }} 月（month.list | length）</li>
      {% endfor %}
    </ul>
  </li>
  {% endfor %}
</ul>

注意这里使用 length 过滤器而不是使用 month.list.count 方法，因为 month.list 已经是不再是一个 QuerySet 对象。
总结

regroup 模板标签对于需要层级分组显示的对象十分有用。但有一点需要注意，被分组的对象一定要是已经有序排列的，否则 regroup 无法正确地分组。相信从以上两个示例中你可以很容易地总结出 regroup 模板标签的用法，从而用于自己的特定需求中，例如像知乎一样对用户每天的通知进行分组显示。




支持 Markdown 语法和代码高亮

    1 年，10 月前 4662 字 53776 阅读 199 评论 

为了让博客文章具有良好的排版，显示更加丰富的格式，我们使用 Markdown 语法来书写我们的博文。Markdown 是一种 HTML 文本标记语言，只要遵循它约定的语法格式，Markdown 的渲染器就能够把我们写的文章转换为标准的 HTML 文档，从而让我们的文章呈现更加丰富的格式，例如标题、列表、代码块等等 HTML 元素。由于 Markdown 语法简单直观，不用超过 5 分钟就可以掌握常用的标记语法，因此大家青睐使用 Markdown 书写 HTML 文档。下面让我们的博客也支持使用 Markdown 书写。
安装 Python Markdown

将 Markdown 格式的文本渲染成标准的 HTML 文档是一个复杂的工作，好在已有好心人帮我们完成了这些工作，我们直接使用即可。首先安装 Markdown，这是一个 Python 第三方库，激活虚拟环境，然后使用命令 pip install markdown 安装即可。
在 detail 视图中渲染 Markdown

将 Markdown 格式的文本渲染成 HTML 文本非常简单，只需调用这个库的 markdown 方法即可。我们书写的博客文章内容存在 Post 的 body 属性里，回到我们的详情页视图函数，对 post 的 body 的值做一下渲染，把 Markdown 文本转为 HTML 文本再传递给模板：

blog/views.py

import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 记得在顶部引入 markdown 模块
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})

这样我们在模板中展示 {{ post.body }} 的时候，就不再是原始的 Markdown 文本了，而是渲染过后的 HTML 文本。注意这里我们给 markdown 渲染函数传递了额外的参数 extensions，它是对 Markdown 语法的拓展，这里我们使用了三个拓展，分别是 extra、codehilite、toc。extra 本身包含很多拓展，而 codehilite 是语法高亮拓展，这为我们后面的实现代码高亮功能提供基础，而 toc 则允许我们自动生成目录（在以后会介绍）。

来测试一下效果，进入后台，这次我们发布一篇用 Markdown 语法写的测试文章看看，你可以使用以下的 Markdown 测试代码进行测试，也可以自己书写你喜欢的 Markdown 文本。假设你是 Markdown 新手参考一下这些教程，一定学一下，保证你可以在 5 分钟内掌握常用的语法格式，而以后对你写作受用无穷。可谓充电五分钟，通话 2 小时。以下是我学习中的一些参考资料：

    Markdown——入门指南
    Markdown 语法说明 (简体中文版)

# 一级标题

## 二级标题

### 三级标题

- 列表项1
- 列表项2
- 列表项3

> 这是一段引用

​```python
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})
​```

如果你发现无法显示代码块，即代码无法换行，请检查代码块的语法是否书写有误。代码块的语法如上边的测试文本中最后一段所示。

你可能想在文章中插入图片，目前能做的且推荐做的是使用外链引入图片。比如将图片上传到七牛云这样的云存储服务器，然后通过 Markdown 的图片语法将图片引入。Markdown 引入图片的语法为：![图片说明](图片链接)。
safe 标签

我们在发布的文章详情页没有看到预期的效果，而是类似于一堆乱码一样的 HTML 标签，这些标签本应该在浏览器显示它本身的格式，但是 Django 出于安全方面的考虑，任何的 HTML 代码在 Django 的模板中都会被转义（即显示原始的 HTML 代码，而不是经浏览器渲染后的格式）。为了解除转义，只需在模板标签使用 safe 过滤器即可，告诉 Django，这段文本是安全的，你什么也不用做。在模板中找到展示博客文章主体的 {{ post.body }} 部分，为其加上 safe 过滤器，{{ post.body|safe }}，大功告成，这下看到预期效果了。

safe 是 Django 模板系统中的过滤器（Filter），可以简单地把它看成是一种函数，其作用是作用于模板变量，将模板变量的值变为经过滤器处理过后的值。例如这里 {{ post.body|safe }}，本来 {{ post.body }} 经模板系统渲染后应该显示 body 本身的值，但是在后面加上 safe 过滤器后，渲染的值不再是body 本身的值，而是由 safe 函数处理后返回的值。过滤器的用法是在模板变量后加一个 | 管道符号，再加上过滤器的名称。可以连续使用多个过滤器，例如 {{ var|filter1|filter2 }}。

Markdown 测试
代码高亮

程序员写博客免不了要插入一些代码，Markdown 的语法使我们容易地书写代码块，但是目前来说，显示的代码块里的代码没有任何颜色，很不美观，也难以阅读，要是能够像我们的编辑器里一样让代码高亮就好了。虽然我们在渲染时使用了 codehilite 拓展，但这只是实现代码高亮的第一步，还需要简单的几步才能达到我们的最终目的。
安装 Pygments

首先我们需要安装 Pygments，激活虚拟环境，运行： pip install Pygments 安装即可。

搞定了，虽然我们除了安装了一下 Pygments 什么也没做，但 Markdown 使用 Pygments 在后台为我们做了很多事。如果你打开博客详情页，找到一段代码段，在浏览器查看这段代码段的 HTML 源代码，可以发现 Pygments 的工作原理是把代码切分成一个个单词，然后为这些单词添加 css 样式，不同的词应用不同的样式，这样就实现了代码颜色的区分，即高亮了语法。为此，还差最后一步，引入一个样式文件来给这些被添加了样式的单词定义颜色。
引入样式文件

在项目的 blog\static\blog\css\highlights\ 目录下应该能看到很多 .css 样式文件，这些文件是用来提供代码高亮样式的。选择一个你喜欢的样式文件，在 base.html 引入即可（别忘了使用 static 模板标签）。比如我比较喜欢 github.css 的样式，那么引入这个文件：

templates/base.html

...
<link rel="stylesheet" href="{% static 'blog/css/pace.css' %}">
<link rel="stylesheet" href="{% static 'blog/css/custom.css' %}">
...
+ <link rel="stylesheet" href="{% static 'blog/css/highlights/github.css' %}">

这里 + 号表示添加这行代码。好了，看看效果，大功告成，终于可以愉快地贴代码了。

代码高亮

注意：如果你按照教程中的方法做完后发现代码依然没有高亮，请依次检查以下步骤：

2017.12.21 更新：完成以上步骤后先退出服务器然后重新 runserver，否则看不到高亮效果

    确保在渲染文本时添加了 markdown.extensions.codehilite 拓展，详情见上文。
    确保安装了 Pygments。
    确保代码块的 Markdown 语法正确，特别是指明该代码块的语言类型，具体请参见上文中 Markdown 的语法示例。
    在浏览器端代码块的源代码，看代码是否被 pre 标签包裹，并且代码的每一个单词都被 span 标签包裹，且有一个 class 属性值。如果没有，极有可能是前三步中某个地方出了问题。
    确保用于代码高亮的样式文件被正确地引入，具体请参见上文中引入样式文件的讲解。
    有些样式文件可能对代码高亮没有作用，首先尝试用 github.css 样式文件做测试。

















