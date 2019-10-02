"""
This is a example settings.py file

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i89n!-gv=7!snicdlre^3v=i0zw3cgbs31@)&wv5gk_g$x1xx3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOCAL_DEBUG = True  # 本地代理static和media可以使用命令python manage.py runserver --insecure

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',  # 会自动 auto-discovery，自动搜索模块下的admin
    'django.contrib.admin.apps.SimpleAdminConfig',  # 当自定义AdminSite时候使用这个, 禁用auto-discovery
    'django.contrib.admindocs',  # admin文档, 需要安装 pip install docutils
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'blog',
    'user',
    'oauth',

    'haystack',  # haystack全文搜索
    'pagedown',  # md编辑器
    'mdeditor',  # md编辑器
    'compressor',  # css/js压缩
    'rest_framework',  # DRF-api
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blog.middleware.LoadTimeMiddleware'  # 页面加载时间
]

# 是否启用django-debug-toolbar. 需要安装: pip install django-debug-toolbar
DJANGO_DEBUG_TOOLBAR = False  # 自己定义的变量, 在urls.py里也需要引入相关路由
if DJANGO_DEBUG_TOOLBAR:  # 还有另一种 django-silk可以尝试用
    # debug工具, 只有在debug=True才生效, 开发环境内使用, 其实可以抽多个settings.develop.py
    INTERNAL_IPS = ['127.0.0.1']
    INSTALLED_APPS += ['debug_toolbar', ]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
    # DEBUG_TOOLBAR_PANELS = []  # 可以自己找更多的插件用

ROOT_URLCONF = 'binblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # 如果需要使用到 MEDIA_URL, 就需要启动这个
                'blog.context_processors.setting',  # 自定义模板全局变量, 网站常量
            ],
        },
    },
]

WSGI_APPLICATION = 'binblog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',  # 数据库名称, 需要自己手动创建, 编码指定为utf8
        'USER': 'root',  # 数据库账号
        'PASSWORD': '123456',  # 数据库密码
        'PORT': 3306,  # 数据库端口, 默认为3306
        'HOST': '127.0.0.1',  # 数据库地址
        'TEST': {
            'NAME': 'test_db',  # 测试数据库名称
            'CHARSET': 'utf8mb4',  # 测试数据库编码
            'COLLATION': 'utf8mb4_general_ci'
        },
        # 查看mysql配置文件加载顺序 mysqld --help --verbose | grep -A1 -B1 cnf
        'OPTIONS': {  # 针对 (mysql.W002) MySQL Strict Mode is not set for database connection 'default'的警告
            'autocommit': True,  # mysql> show variables like '%autocommit%';
            # 严格模式文档: https://dev.mysql.com/doc/refman/5.6/en/sql-mode.html
            # 开启mysql严格模式, 5.6后是默认值NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
            'init_command': "SET sql_mode='NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES'",
        },
    }
}

# 密码验证类 Password validation
# https://docs.djangoproject.com/en/2.1/topics/auth/passwords/
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        # 检查密码和用户名是否具有相似性
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # 检查密码长度
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    # {   # 密码是否非常常用，会比较20000个常用密码
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {   # 是否是纯数字
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # timeit shows that datetime.now(tz=utc) is 24% slower

# sitemap指定站点, 对应数据表django_site中的id
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'  # url上显示的静态文件目录127.0.0.1:8080/static/1.jpg
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')  # 执行静态资源收集后存储的目录
STATICFILES_DIRS = (  # 多个存储静态资源的目录
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'  # url上显示的静态文件目录127.0.0.1:8080/static/1.jpg
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# compress压缩静态文件设置
COMPRESS_ENABLED = True  # 开启Compressor，因为默认是和DEBUG相反，用于生产环境，显式启动
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',  # 默认开启的, 磁盘中查找
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',  # 默认开启的, app目录中查找
    'compressor.finders.CompressorFinder',  # compress的
)

# 用户类
AUTH_USER_MODEL = 'user.UserProfile'
AUTHENTICATION_BACKENDS = (
    # https://docs.djangoproject.com/en/2.1/ref/contrib/auth/#django.contrib.auth.models.User.is_active
    # 'django.contrib.auth.backends.AllowAllUsersModelBackend',  # 验证is_active, 会显示未激活, 否则会显示账号密码错误
    'user.backends.LoginByUsernameOrEmailBackend',  # 可以根据邮箱或者用户名登陆, 集成了 AllowAllUsersModelBackend
)

# 使用haystack进行文章搜索
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'utils.whoosh_cn_backend.WhooshEngine',  # 自定义使用jieba进行中文分词
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
    # 如果要使用Es2作为搜索引擎, 因为看过django-haystack的github, 目前最新版2.8.1只支持Es1.x和Es2.x
    # 新的发行版由于作者一直没有更新, github源码中的backend里有支持Es5.x的, 不过自己不够强emmm
    # 观察了issue, 原作者时间不够, 希望自己以后对Es深入后有实力去贡献代码, add oil
    # 1. 下载安装Es(依赖于java) https://www.elastic.co/cn/downloads/past-releases/elasticsearch-2-4-1
    # 2. 安装对应版本的Es包 pip install elasticsearch==2.4.1
    # 3. 启动Es, 下载解压后进入bin目录启动bat即可(win), 之后python manage.py rebuild_index重建索引
    # 4. 其他不变, runserver后进行搜索尝试, 默认支持了中文分词搜索的, 奇了怪了hhh
    # 5. 研究了Es7和elasticsearch-dsl, 不过自己本地上还是测试失败, 于是放弃折腾了, 使用了Es2, 以后好好学下Es
    # 'default': {
    #     'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
    #     'URL': 'http://127.0.0.1:9200/',  # Es默认使用的是9200端口
    #     'INDEX_NAME': 'blog',  # 索引名称
    # },
}
# 自动更新搜索索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 发送邮件的配置
EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'user@sina.com'  # Your email username
EMAIL_HOST_PASSWORD = 'sina123456'  # Your email password
EMAIL_USE_TLS = False  # 不使用TLS协议, 不https:443
EMAIL_FROM = 'BinBlog<binloveplay1314@sina.com>'  # 发件人

# 缓存设置,想在本地看到是否有效,可以实时更改数据库里的数据,缓存里的数据不会变
# 环境里有memcached就可以使用memcached进行缓存，没有就使用本地缓存
CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',  # memcached缓存
    #     'LOCATION': '127.0.0.1:11211',
    #     'TIMEOUT': 60 * 60 * 1,  # 过期时间 单位为秒
    # },
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    #     'LOCATION': 'django_cache',
    # },
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # 本地内存缓存
        'TIMEOUT': 60 * 60 * 1,  # 过期时间 秒, 一个钟过期
        'LOCATION': 'unique-snowflake',
    }
}

# logging的配置 https://docs.djangoproject.com/en/2.2/topics/logging/
SERVER_EMAIL = EMAIL_HOST_USER  # 发送错误信息时的邮箱
ADMINS = [('bin', 'binloveplay1314@qq.com')]  # 管理员元组列表, 500错误邮件通知
BASE_LOG_DIR = os.path.join(BASE_DIR, 'log')  # 日志存放的目录, 需要手动创建
LOG_PREFIX = 'binblog_'  # 日志文件命名前缀
LOGGING = {  # 开发中有用的信息 < 常规操作中有用的信息 < 有问题的警告但不紧要 < 重要的错误信息 < 高于错误的关键信息
    # 日志等级: DEBUG < INFO < WARNING < ERROR < CRITICAL
    # 日志处理流程简易版本:
    # 1) 首先先判断日志是否满足日志器设置的等级
    # 2) 接着根据过滤器过滤日志
    # 3) 然后判断日志是否满足处理器设置的等级
    # 4) 有多个处理器就重复上面的判断
    # 5) 根据propagate判断日志是否需要传递给上级日志器
    'version': 1,  # 保留字, 只能为1
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    # 格式器, 决定日志记录的输出格式
    'formatters': {
        # 详细的日志格式, 用于记录到日志文件里
        'verbose': {
            # [2019-05-27 16:07:10,530] ERROR [root.get_queryset:25 views] 11
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d %(module)s] %(message)s',
        },
        # 简单的日志格式, 用于console输出
        'simple': {
            'format': '{levelname} {message}',
            'style': '{'  # format的格式 {}
        },
    },
    # 过滤器, 提供更细粒度的工具决定哪些日志会输出
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',  # 要求debug=True
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    # 处理器, 将日志器创建的日志记录发送到合适的目的输出
    'handlers': {
        'console': {  # console终端输出打印
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'  # 控制台就打印简单的格式日志
        },
        'mail_admins': {  # error, 邮件输出通知管理员
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],  # 上线状态debug=False才处理
            'include_html': True,  # 邮件显示以html格式显示, 跟debug=True时的窗口一致
        },
        'default': {  # 默认的输出写入文件保存
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'filename': os.path.join(BASE_LOG_DIR, LOG_PREFIX + "info.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 10,  # 日志大小 10M
            'backupCount': 3,  # 最多备份几个
            'encoding': 'utf-8',
            'formatter': 'verbose',
        },
        'error': {  # 错误级别的也输出到文件保存
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, LOG_PREFIX + "error.log"),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
            'encoding': 'utf-8',
            'formatter': 'verbose',
        }
    },
    # 日志器, 提供引用程序可使用的接口
    'loggers': {  # logging.getLogger
        '': {  # '': root logger 处理logger日志, 高于info等级就都用console显示, error级别的就再写入文件
            'handlers': ['console', 'error'],
            'level': 'INFO',
        },
        'django': {  # django名称的, 默认将处理所有log
            'handlers': ['default'],  # 个人调试不看DEBUG
            # 'handlers': ['console', 'default'],  # 调试的时候看情况输出控制台, 不然DEBUG信息太多了, 主要可以看到sql
            'level': 'DEBUG',
            'propagate': False,  # 向不向更高级别的logger传递, 避免root logger双重日志记录
        },
        'django.request': {  # django.request的, 会自动处理服务器500错误
            'handlers': ['mail_admins'],
            'level': 'ERROR',
        },
        'django.template': {  # django.template, 这里设置为info, 屏蔽admin_login时候的DEBUG信息
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# celery的配置, 查看binblog.celery.py里的注释
# 字库自定义, 一个redis实例下有16个字库, 在redis-cli中使用 select 7 切换字库, keys * 查看所有的key, get key 查看key的数据
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/7'  # 消息传输中间人(任务队列), 一般用RabbitMQ(消息队列) 或者 redis
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/8'  # 数据库存储任务执行结果, 一般用redis
CELERY_TASK_SERIALIZER = 'json'  # 任务序列化为json, 或者有使用pickle的
CELERY_RESULT_SERIALIZER = 'json'  # 任务结果序列化为json格式
CELERY_ACCEPT_CONTENT = ['json']  # 指定任务接收的序列化类型 [pickle, json, yaml, msgpack]

# Django REST framework配置
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',  # json render
        'rest_framework.renderers.BrowsableAPIRenderer',  # drf浏览器render
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',  # 默认为 AllowAny
    )
}

# curl 测试jwt, 根据username和password返回了一个 token
# curl -X POST -d "username=bin&password=1123" http://127.0.0.1:8000/api/auth/token/
# {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImJpbiIsImV4cCI6MTU1MjU2MzcyOCwiZW1haWwiOiJiaW5sb3ZlcGxheTEzMTRAcXEuY29tIn0.51CSDqWxiXwxMkuxm8zpCn1SJyI7eapt3Vt1cFFp4aI"}

# 测试命令, 注意权限的设置
# curl -H "Authorization: JWT <your_token>" http://127.0.0.1:8000/api/blog/article/

# 不使用JWT, 返回不到信息
# curl http://127.0.0.1:8000/api/blog/article/

# 带上jwt返回信息成功
# curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImJpbiIsImV4cCI6MTU1MjU2MzcyOCwiZW1haWwiOiJiaW5sb3ZlcGxheTEzMTRAcXEuY29tIn0.51CSDqWxiXwxMkuxm8zpCn1SJyI7eapt3Vt1cFFp4aI" http://127.0.0.1:8000/api/blog/article/

# 测试POST数据，不加JWT，注意权限的设置 AllowAny
# curl -X POST -d "{\"name\": \"a new category\"}" -H "Content-Type:application/json" -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImJpbiIsImV4cCI6MTU1MjU2MzcyOCwiZW1haWwiOiJiaW5sb3ZlcGxheTEzMTRAcXEuY29tIn0.51CSDqWxiXwxMkuxm8zpCn1SJyI7eapt3Vt1cFFp4aI" http://127.0.0.1:8000/api/blog/category/create/
# 测试POST数据，加了JWT,设置权限需要登陆
# curl -X POST -H "Content-Type: application/json" -d '{\"name\":\"A new category\"}' -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImJpbiIsImV4cCI6MTU1MjU2MzcyOCwiZW1haWwiOiJiaW5sb3ZlcGxheTEzMTRAcXEuY29tIn0.51CSDqWxiXwxMkuxm8zpCn1SJyI7eapt3Vt1cFFp4aI" http://127.0.0.1:8000/api/blog/category/create/
