from binblog.settings_example import *

# 覆盖原先settings里的一些配置
# https://docs.travis-ci.com/user/database-setup/
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',  # 数据库名称, 对应travis.yml里的数据库名称
        'USER': 'root',  # 数据库账号 travis里是 travis或者root
        'PASSWORD': '',  # 数据库密码 travis里是 留空
        'PORT': 3306,  # 数据库端口, 默认为3306
        'HOST': '127.0.0.1',  # 数据库地址
        'TEST': {
            'NAME': 'test_db',  # 测试数据库名称
            'CHARSET': 'utf8',  # 测试数据库编码
            'COLLATION': 'utf8_general_ci'
        }
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'django_cache',
    }
}
