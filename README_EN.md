# BinBlog

### Demo Address：http://13.58.211.105/

A blog system based on `python3.6` and `Django2.1`

- [Chinese_README](./README.md)

[![license](https://img.shields.io/github/license/enjoy-binbin/Django-blog.svg)](https://github.com/enjoy-binbin/Django-blog/blob/master/LICENSE) [![Build Status](https://travis-ci.com/enjoy-binbin/Django-blog.svg?branch=master)](https://travis-ci.org/enjoy-binbin/Django-blog) [![codecov](https://codecov.io/gh/enjoy-binbin/Django-blog/branch/master/graph/badge.svg)](https://codecov.io/gh/enjoy-binbin/Django-blog) [![Coverage Status](https://coveralls.io/repos/github/enjoy-binbin/Django-blog/badge.svg?branch=master)](https://coveralls.io/github/enjoy-binbin/Django-blog?branch=master) [![Requirements Status](https://requires.io/github/enjoy-binbin/Django-blog/requirements.svg?branch=master)](https://requires.io/github/enjoy-binbin/Django-blog/requirements/?branch=master)

### Development Env

What i use in this blog system.

1. DEBUG system: win10 x64
2. Python related：Python3.6、Django2.1、Djangorestframework 3.9、Celery4
3. DB：localize: Mysql，cache: Memcache，MQ: Redis
4. html related：Jquery、Bootstrap ...
5. IDE：PyCharm 2018.1
6. Web system： AWS ，Ubuntu18.04，Nginx+(gunicorn or uwsgi)，Mysql5.7，Python3.6
7. The online code is out of sync and has been developing locally

## Main function

* Secondary development of the admin site
* Category、Aritcle、Tag、Comment、Paginator、
* Article editing support `Markdown
* User register and login，emal authentication，Github login
* Sitebar、Hot articles、New articles、Tag cloud、Site map、RSS
* Articles are archived according to the time they were added
* API development for blogs with the Djangorestframework (in the blog/ API directory)
* Using logging record error log，Using  celery + redis for asynchronous tasks scheduling
* Multi-user blogging system，blog user can post a common article，also can do CURD
* A photo album function

## What i used

* Djangorestframework and Restframework-jwt do some Api
* Django generic views like ListViewDetailView，FromView，RedirectView...
* Secondary development of the admin site
* Custom LoginView，RegisterView，LogoutView，learn some django.auth
* Context_processors custom template global var
* Support Markdown
* Templatetags custom tags
* Full-text search using haystack and whoosh
* How to use slug
* Use django-compress to compress CSS  and  JS files
* Writing django simple middleware that shows page load times
* Use django's sitemap function
* Python-memcached caches parts of your site's information
* Custom django.manage  comand - create_fake_data can create some test data
* Using logging and message 
* Using celery and MQ:redis post emai

## Install

You can simply run this command to install all package

```
pip install  -r requirements.txt
```

Then copy a settings file 

```
cp ./binblog/settings.py.example ./binblog/settings.py
```

Change `binblog/settings.py` db conf:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',  # Your db name utf8
       	# create database blog default character set utf8 collate utf8_general_ci;
        'USER': 'root',  # Your db username
        'PASSWORD': '123456',  # Your db password
        'PORT': 3306,  # db port
        'HOST': '127.0.0.1',
        'TEST': {
            'NAME': 'test_db',  # test_db name for test
            'CHARSET': 'utf8',  # encoding
            'COLLATION': 'utf8_general_ci'
        }
    }
}
```

Do makemigrations && migrate:

```
python manage.py makemigrations
python manage.py migrate
```

You can also create some fake data to display, simply run this comand

```
python manage.py create_fake_data
```

You can also import a sql file , but the content is chinese...

At last，run the command below:

```
python manage.py runserver 8000
```

And open your browser and visit 127.0.0.1:8000

There are more conf item in the settings.py and the blog.model.Setting. But it also Chinese, sorry, maybe someday i will rewrite on the furture

### Thanks for reading and star，also welcome post a issue or Email

Also forgive my pool english lol. But i am working on it . Thank you so much~

#### Some demo 

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/media/display/display.png)

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/media/display/display2.png)

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/media/display/display3.png)

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/media/display/display4.png)

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/media/display/display5.png)

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/media/display/display6.png)

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/media/display/display7.png)

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/media/display/display8.png)

![display](https://github.com/enjoy-binbin/binblog-Django/blob/master/media/display/display9.png)
