import os
import sys
import shutil

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    """ run python manage.py clear_migrations
        清理migrations的迁移文件, 后自动再进行初始化迁移
        也就是在不影响自己数据库数据的前提下, 清理app/migrations下的所有迁移文件
    """
    help = 'Clear all migrations files in project and auto migrate --fake-initial'

    def handle(self, *args, **options):
        def get_app():
            """ 获取settings里的所有app """
            for app in settings.INSTALLED_APPS:
                path = os.path.join(settings.BASE_DIR, app.replace(".", "/"), "migrations")
                if os.path.exists(path):
                    yield app, path

        def clear(path):
            shutil.rmtree(path)  # 递归删除目录
            os.makedirs(path)
            with open(os.path.join(path, "__init__.py"), "w+") as ff:
                # 创建__init__包文件
                pass

        # 执行命令migrate --fake app zero
        for app_name, app_path in get_app():
            # D:\A-python\Django-blog\env\Scripts\python.exe manage.py migrate --fake user zero
            os.system(f"{sys.executable} manage.py migrate --fake {app_name} zero")  # sys.executable 当前python解释器

        # 和上面分开写, 先fake全部app后再clear, 防止 Dependency on app with no migrations: [app]错误
        for app_name, app_path in get_app():
            clear(app_path)
            self.stdout.write(self.style.SUCCESS(f"\nClear app: {app_name} migrations done\n"))

        # 进行初始化的迁移 python manage.py migrate --help 查看帮助信息
        self.stdout.write(self.style.SUCCESS('\nRunning makemigrations and migrate --fake-initial\n\n'))
        os.system(f"{sys.executable} manage.py makemigrations")
        os.system(f"{sys.executable} manage.py migrate --fake-initial")

        self.stdout.write(self.style.SUCCESS('\nSuccessfully cleared!'))
