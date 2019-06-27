#### 简要说明

依赖配置文件中的配置

```
STATIC_URL = '/static/'  # url上显示的静态文件目录127.0.0.1:8080/static/1.jpg
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')  # 执行静态资源收集后存储的目录
STATICFILES_DIRS = (  # 多个存储静态资源的目录
    os.path.join(BASE_DIR, 'static'),
)
```



用于生产环境收集静态文件，然后给nginx进行统一代理。

*下面命令将STATICFILES_DIRS目录下的所有静态文件收集到STATIC_ROOT目录下*

```
python manage.py collectstatic
```