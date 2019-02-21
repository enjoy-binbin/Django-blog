# 未完成

## 我的开发环境:  先简单的来，前后端不分离。时间 19年1月

1. win10 64位
2. python 3.6
3. Django 2.1
4. Mysql 5.6
5. PyCharm 2018.1
6. xadmin后台： `bin 1123`

### 使用到
* admin的扩展，ModelAdmin的使用
* django通用视图, ListView, DetailView
* context_processors自定义模板全局变量
* admin编辑页 TextFields使用 `pagedow`n 支持 `markdown`
* templatetags 自定义模板标签 tags
* logger记录日志
* cache的使用
* 使用haystack和whoosh实现搜索功能


### 新建虚拟环境
	cmd > makevirtualenv binblog
	cmd > workon binblog

### 创建数据库
	mysql > create databases binblog;

### 安装django2.1
	pip install django==2.1.5 -i https://pypi.douban.com/simple

### 用django创建项目
	cmd > django-admin startproject binblog

### 安装mysql和settings配置mysql数据库
	pip install -i https://pypi.douban.com/simple mysqlclient==1.4.1
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': 'binblog',
	        'USER': 'root',
	        'PASSWORD': '1123',
	        'HOST': '127.0.0.1'
	    }
	}

### 在settings里设置模板文件dir
    'DIRS': [os.path.join(BASE_DIR, 'templates')],

### 静态资源
	STATIC_URL = '/static/'  # url上显示的静态文件目录127.0.0.1:8080/static/1.jpg
	# STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')  # 执行静态资源收集后存储的目录
	STATICFILES_DIRS = (  # 多个存储静态资源的目录
	    os.path.join(BASE_DIR, 'static'),
	)



### 对admin的扩充



### 安装django-pagedown
	# github地址: https://github.com/timmyomahony/django-pagedown
	pip install django-pagedown
	Add `pagedown` to the `INSTALLED_APPS`
	用法看文档，提供一个easy addition of Stack Overflow's "Pagedown" Markdown editor


### 使用MemcachedCache和本地内存缓冲
	# settings.py
	# 使用python-memcached绑定在127.0.0.1:11211
	CACHES = {
	    'default': {
	        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
	        'LOCATION': '127.0.0.1:11211',
			'TIMEOUT': 10800,
	    }
	}
	
	# 本地内存缓冲，如果在settings里未指定，则是默认缓冲
	CACHES = {
	    'default': {
	        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
	        'LOCATION': 'unique-snowflake'
	    }
	}




### templatetags 自定义标签或者过滤器
	# 在blog目录下创建 templatetags目录 再创建 blog_tags.py




