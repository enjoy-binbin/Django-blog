# BinBlog

### 演示地址：http://13.58.211.105/

基于 `python3.6` 和 `Django2.1`的博客系统

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/display.png)

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/display2.png)

### 本地开发环境

1. win10 64位
2. python 3.6
3. Django 2.1
4. Mysql 5.6
5. PyCharm 2018.1
6. Djangorestframework 3.9
7. admin后台： `bin 1123`
8. 线上环境： AWS ，Ubuntu18.04，Mysql5.7, Python3.6

## 主要功能

* 文章分类，文章，文章标签的增删改查，展示
* 文章详情支持`Markdown`，支持代码高亮
* 支持文章列表分页
* 文章评论功能
* admin后台管理系统
* 用户注册登陆，支持github oauth登陆
* 右侧侧边栏功能，最热文章，最新文章，标签云
* 文章根据添加时间进行归档
* 使用Djangorestframework对博客进行API开发（在blog/api目录下）

## 使用到

* djangorestframework和 restframework-jwt进行API学习开发
* django通用视图，ListViewDetailView，FromView，RedirectView
* admin的扩展，ModelAdmin扩展，SimpleListFilter自定义过滤器
* 自定义LoginView，RegisterView，LogoutView，部分django自带auth用法
* context_processors自定义模板全局变量
* 侧边栏编辑页 TextFields使用 `pagedown` 支持 `markdown`
* 文章内容使用 `mdeditor`支持`markdown`和`图片上传`
* templatetags 自定义模板标签 tags，支持markdown，代码高亮
* 使用haystack和whoosh实现的全文文章搜索功能
* slug的用法
* 使用django-compress压缩css/js
* django简单中间件的编写，显示页面加载时间
* 使用django的sitemap功能
* python-memcached对网站的部分信息缓存
* 自定义django.manage命令,create_testdata，生成测试数据

## TOLearn

终于有服务器拉， 下次准备 集成 Oauth登陆，之前一直没有服务器做测试

## 安装

1. 安装依赖（最好新建个虚拟环境）
   * pip install -Ur requirements -i https://pypi.douban.com/simple
2. 配置设置将settings.py.example改成 settings.py
  * 自行修改 `binblog/settings.py` 里的数据库配置:
     DATABASES = {
     	    'default': {
     	        'ENGINE': 'django.db.backends.mysql',
     	        'NAME': 'binblog',
     	        'USER': 'root',
     	        'PASSWORD': '123456',
     	        'HOST': '127.0.0.1'
     	    }
     	}
  * 创建数据库 `create database binblog;`
  * 在终端下进行数据迁移:
       `./manage.py makemigrations`
          ` ./manage.py migrate`
  * 创建测试数据 `./manage.py create_testdata`
  * 根据需要使用Navicat导入目录下的 sql文件
      `./ manage.py createsuperuser`
  * 运行 `./manage.py runserver 8000`
  * 浏览器打开 `127.0.0.1:8000`
3. 配置项（更多设置看settings和blog.model.Setting模型）

### 更多笔记在 notes里。标准的md格式，源码中也有大量注释。

### 感谢观看和star，欢迎提issue

