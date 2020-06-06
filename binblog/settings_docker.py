# 用于在docker中运行, 在docker中我设置会将此文件重命名为settings.py用于docker的部署
from binblog.settings_example import *

DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', 'yes', 'y')

# 覆盖原先settings里的一些配置
# https://docs.travis-ci.com/user/database-setup/
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'binblog',  # 数据库名称
    'USER': 'root',  # 数据库账号
    'PASSWORD': 'ppp1123',  # 数据库密码, 根据docker里的设置
    'PORT': 3306,  # 数据库端口, 默认为3306
    'HOST': 'mysql',  # 数据库地址, 对应docker里容器的命名
    'TEST': {
        'NAME': 'test_db',  # 测试数据库名称
        'CHARSET': 'utf8',  # 测试数据库编码
        'COLLATION': 'utf8_general_ci'
    }
}
for db in DATABASES:
    if db == "default":
        continue
    DATABASES[db] = DATABASES["default"]

CACHES['default'] = {
    "BACKEND": "django_redis.cache.RedisCache",
    "LOCATION": "redis://redis:6379/0",
    "OPTIONS": {
        "CLIENT_CLASS": "django_redis.client.DefaultClient",
    }
}
for cache in CACHES:
    if cache == "default":
        continue
    CACHES[cache] = CACHES["default"]
