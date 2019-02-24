

# BinBlog

基于 `python3.6` 和 `Django2.1`的博客系统

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/display.png)

### 本地开发环境

1. win10 64位
2. python 3.6
3. Django 2.1
4. Mysql 5.6
5. PyCharm 2018.1
6. admin后台： `bin 1123`

## 主要功能

* 文章分类，文章，文章标签的增删改查，展示
* 文章详情支持`Markdown`，支持代码高亮
* 支持文章列表分页
* 文章评论功能
* admin后台管理系统
* 用户注册登陆
* 右侧侧边栏功能，最热文章，最新文章，标签云
* 文章根据添加时间进行归档

## 使用到

* django通用视图，ListViewDetailView，FromView，RedirectView
* admin的扩展，ModelAdmin扩展，SimpleListFilter自定义过滤器
* 自定义LoginView，RegisterView，LogoutView，部分django自带auth用法
* context_processors自定义模板全局变量
* admin编辑页 TextFields使用 `pagedown` 支持 `markdown`
* templatetags 自定义模板标签 tags，支持markdown，代码高亮
* 使用haystack和whoosh实现的全文文章搜索功能
* slug的用法
* 使用django-compress压缩css/js
* django简单中间件的编写，显示页面加载时间
* 使用django的sitemap功能

## 将学习

集成 Oauth登陆，使用缓冲。。。。

## 安装

1. 安装依赖（最好新建个虚拟环境）
   * pip install -Ur requirements -i https://pypi.douban.com/simple
2. 配置设置
  * 自行修改 `binblog/settings.py` 里的数据库配置:
     DATABASES = {
     	    'default': {
     	        'ENGINE': 'django.db.backends.mysql',
     	        'NAME': 'binblog',
     	        'USER': 'root',
     	        'PASSWORD': '1123',
     	        'HOST': '127.0.0.1'
     	    }
     	}
  * 创建数据库 `create database binblog;`
  * 在终端下进行数据迁移:
      	./manage.py makemigrations
            	./manage.py migrate
  * 根据需要使用Navicat导入目录下的 sql文件
    		./ manage.py createsuperuser
  * 运行 `./manage.py runserver 8000`
  * 浏览器打开 `127.0.0.1:8000`
3. 配置项（更多设置看settings和blog.model.Setting）

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




