# 基础镜像, 一个镜像Dockerfile必需的
FROM daocloud.io/python:3.6

# 维护者信息, 可以写邮箱网站啥的
MAINTAINER binbin <binloveplay1314@qq.com>

# ADD、COPY将目录里的文件拷贝到镜像中, ADD会自动解压
# 适用于自己有项目tar包里, 里面的配置信息例如settings都弄好了
# ADD blog.tar.gz /var/www

# 设置工作目录, 容器会自动cd到这里
WORKDIR /var/www

# 下载blog项目, 或者可以自己ADD, /var/www/Django-blog/
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY sources.list /etc/apt
RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/enjoy-binbin/Django-blog.git

# 复制配置文件
RUN cp ./Django-blog/binblog/settings_docker.py ./Django-blog/binblog/settings.py

RUN pip install --upgrade pip

# 安装依赖, 使用阿里云镜像
RUN pip install --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple/ -r ./Django-blog/requirements.txt --trusted-host mirrors.aliyun.com

RUN pip install --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com gunicorn

WORKDIR /var/www/Django-blog

CMD python manage.py makemigrations; python manage.py migrate; python manage.py create_fake_data; python manage.py collectstatic --noinput; python manage.py compress --force; gunicorn binblog.wsgi --bind 0.0.0.0:8000