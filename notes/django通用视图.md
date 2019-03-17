```
from django.views.generic xxx
```

1. 展示对象列表（文章列表）- ListView

1. 展示某个对象的详细信息（文章详情) - DetailView

1. 通过表单创建某个对象（比如创建用户，新建文章）- CreateView

1. 通过表单更新某个对象信息（比如修改密码，修改文字内容）- UpdateView

1. 用户填写表单后转到某个完成页面 - FormView

1. 删除某个对象 - DeleteView



#### 只展示这些吧，其他的建议看官方文档

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


