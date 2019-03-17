# 使用`django-compressor`，压缩 css/js

2019年2月22日 10:22:23

将静态文件压缩并合并成一个文件，减少网站请求次数，节省网络带宽

github地址: https://github.com/django-compressor/django-compressor

文档地址: https://django-compressor.readthedocs.io/en/latest/quickstart/



### 补充：Settings文件静态资源配置详解

新版的Django都有将  `django.contrib.staticfiles` 加入内置app

### 1. STATIC_URL
settings里： ```STATIC_URL = '/static/' ```

STATIC_URL是浏览器访问静态资源时路径，比如：模版中定义的资源路径是：

```python
{% load static %}
<script src="{% static "css/style.css" %}"></script>

# 最后实际渲染出来的是：
<script src="/static/css/style.css"></script>

# url上显示的静态文件目录127.0.0.1:8080/static/css/style.css
# 可以自己指定, 没有强制规定为 static，不过一般约定俗成
```

### 2. STATICFILES_DIRS，多个存储静态资源的目录

```python
# settings里
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '其他存放静态文件的目录, 例如一些共用包，可以放在磁盘上的任意位置(有权限访问)',
)
```
### 3. STATIC_ROOT，收集静态资源的目录

在生产环境下，就需要使用到这个了，作用是收集项目里所有的静态文件，将其收集到统一目录下，然后使用Nginx代理这些静态文件，在开发环境中可以不指定，而且不能是STATICFILES_DIRS里的元素

```python
# settings里
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')

# 运行collectstatic管理命令
python ./manage.py collectstatic

# 而后所有静态资源将都会统一的收录到 collectstatic 目录下
```

### 4. 静态文件的finder，默认有的

```python
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
	"django.contrib.staticfiles.finders.AppDirectoriesFinder"
)
# AppDirectoriesFinder就是负责在各个app/static目录下查找静态文件。
# FileSystemFinder就是用来查找定义在STATICFILES_DIRS中的静态文件的。
```



## 使用django-compressor压缩静态文件

### 1. 安装

```pip install django-compressor==2.2```

### 2. 配置

settings里的配置:

```
INSTALLED_APPS = (
    # other apps
    "compressor",
)

COMPRESS_ENABLED = True  # 开启Compressor，因为默认是和DEBUG相反，用于生产环境，显式启动

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')  # 执行静态资源收集后存储的目录
```

### 3. 使用

* 在模板文件中添加模板标签 `{% load compress %}`
* 将需要压缩的css和js分别用 {% compress css %}{% endcompress %}包裹

```html
{% load compress %}

{% compress css %}
<link href="{% static "css/base.css" %}" rel="stylesheet">
<link href="{% static "css/style.css" %}" rel="stylesheet">
{% endcompress %}

{% compress js %}
<script src="{% static "js/style.js" %}"></script>
<script src="{% static "js/blog.js" %}"></script>
{% endcompress %}
```

* 启动项目查看渲染后的样子

  ```html
  <link rel="stylesheet" href="/static/CACHE/css/25fb70e47f11.css" type="text/css" />
  <script type="text/javascript" src="/static/CACHE/js/c71e77581f2f.js"></script>
  ```

* 同时项目目录下出现 `STATIC_ROOT`里设置的目录，并且压缩后的文件都存放在这的CACHE下

* 修改静态文件后，项目重启会自动压缩并更新在CACHE里的压缩文件

### 4. 不知道生产环境下是否需要(还没尝试) TODO

```
python manage.py collectstatic
python manage.py compress --force
```

