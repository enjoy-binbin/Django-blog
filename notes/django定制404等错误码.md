### django2 项目定制404等错误码

2019年2月25日 12:05:35

文档地址：`https://docs.djangoproject.com/en/2.1/topics/http/views/#customizing-error-views`

### 准备工作，要想要django显示404等错误页，需要关闭DEBUG模式

在settings.py里将调试模式关闭，以及设置可以访问的主机

```
DEBUG = False

ALLOWED_HOSTS = ['*']
```

因为django默认对静态文件的处理，在上线模式是不会对静态文件进行处理的

所以在运行项目的时候得使用 `python manage.py runserver --insecure`，这样就可以看到404页面了

### 使用

在blog.views(自定义哪个app下都可以)里编写如下代码：

```python
from django.shortcuts import render

def permission_denied(request, exception, template_name='blog/error_page.html'):
    """ 处理403错误码 """
    error_msg = '403错误拉，没有权限访问当前页面，点击首页看看别的？'
    return render(request, template_name, {
        'error_msg': error_msg,
    }, status=403)


def page_not_found(request, exception, template_name='blog/error_page.html'):
    """ 处理404错误码 """
    url = request.get_full_path()
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
```

urls.py路由文件下的配置：

```python
# 添加如下代码，和前面所写的方法对应即可
handler403 = 'blog.views.permission_denied'
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'
```

模板文件error_page.html就是简单的展示你的 error_msg即可，跟其他模板文件一样的编写方式