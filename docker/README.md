#### Docker + nginx + mysql + Django 部署博客

#### 快速安装

```
# 说明, 本仓库里存放的只是docker相关的文件
# 使用到的镜像nginx:1.14、python3.6、mysql5.6.30
# django-blog项目是拉取另外个仓库(可以的话点个star，非常感谢): 
	https://github.com/enjoy-binbin/Django-blog
# 使用到的镜像有daocloud.io/nginx:1.14、daocloud.io/python:3.6、daocloud.io/mysql:5.6.30
# 再下面有自己的笔记步骤，最后的体验。这几个镜像里用到了ubuntu/centos/debian
# 自己前后弄了好几天，docker使用没有多久，项目并不是最佳实践，仅供学习。

# 克隆本项目
git clone https://github.com/enjoy-binbin/docker-django-blog.git

# 执行脚本
source docker-django-blog/start.sh
```

![display](https://raw.githubusercontent.com/enjoy-binbin/docker-django-blog/master/display.png)



#### 笔记部分

##### 1. 准备相关环境

自己在虚拟机上Centos7.6测试成功。假如你是个公网服务器，可以跳过这第一步

设置阿里源，虚拟机里设置的是Nat网络

```shell
cd /etc/yum.repos.d

yum install -y wget
# 下载阿里源yum源
wget -4 http://mirrors.aliyun.com/repo/Centos-7.repo

# 备份原有CentOS-Base.repo
# 将阿里源命名为CentOS-Base.repo
mv CentOS-Base.repo CentOS-Base.repo.bak
cp Centos-7.repo CentOS-Base.repo

yum clean all
yum makecache

yum -y install vim
```

##### 2. 安装Docker

```
# 参考链接：https://www.runoob.com/docker/centos-docker-install.html
# 安装一些必要的系统工具
sudo yum install -y yum-utils device-mapper-persistent-data lvm2

# 添加软件源信息：
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

# 更新 yum 缓存：
yum makecache fast

# 安装 Docker-ce：
sudo yum -y install docker-ce

# 启动 Docker 后台服务
systemctl start docker

# docker hello world
docker run hello-world
```

##### 3. 镜像加速

鉴于国内网络问题，后续拉取 Docker 镜像十分缓慢，我们可以需要配置加速器来解决，我使用的是网易的镜像地址：**http://hub-mirror.c.163.com**。

vim /etc/docker/daemon.json（Linux）请在该配置文件中加入（没有该文件的话，请先建一个）：

```
{
  "registry-mirrors": ["http://hub-mirror.c.163.com"]
}
```

使用`docker info` 观察输出



#### 正文部分，使用Docker部署Django-blog项目

容器的创建顺序：mysql -> django-web -> nginx。其中django会依赖于mysql的数据库，nginx会转发django中的静态文件资源。docker容器，单个容器提供单个服务，当然也可以将服务全部写到一个镜像容器中。



##### 1. 先拉取后面需要用到的镜像

拉取Docker官方镜像的时候如果慢可以使用 daocloud.io源，例如 daocloud.io/python:3.6

```
docker pull daocloud.io/nginx:1.14
docker pull daocloud.io/python:3.6
docker pull daocloud.io/mysql:5.6.30
```



##### 2. 创建mysql容器

在mysql目录中只有一个shell脚本文件，根据镜像run一个mysql容器，并且设置明密码为123456，创建blog库

```shell
#!/bin/bash

# 启动mysql容器(先mysql、再django-blog、再nginx)
# --name mysql 启动后的容器名称
# -p 3307:3306 端口映射, 将mysql容器的3306端口映射到主机的3307(因为自己主机3306有个mysql)
# -e MYSQL_ROOT_PASSWORD=123456 配置的Mysql密码
# -v $PWD/conf:/etc/mysql/conf.d 将当前目录下的/conf文件夹挂在到容器里的/etc/mysql/conf.d, 如果自己有配置文件需要这样挂载
# -v $PWD/data:/var/lib/mysql 将当前目录下的data目录挂载到容器的 /var/lib/mysql, 还有其他文件同理
# -d 运行在后台
# daocloud.io/mysql:5.6.30 对应的镜像名称
#
echo "---------Start mysql image---------"
#
docker run --name mysql \
-p 3307:3306 \
-e MYSQL_ROOT_PASSWORD=123456 \
-d daocloud.io/mysql:5.6.30 
#
# 这里要睡一会才好创建数据库, 之前睡太短一直出错/难受
sleep 10
# docker exec 执行mysql容器里的mysql命令 创建数据库
docker exec -it mysql mysql -uroot -p123456 -e "create database blog default character set utf8 collate utf8_general_ci;"
#
echo "---------End mysql image---------"
#
# 进入容器的方法 mysql 容器名
# docker container inspect --format "{{.State.Pid}}" mysql
# docker inspect --format "{{.State.Pid}}" mysql
# 37834
#
# nsenter参数说明: http://man7.org/linux/man-pages/man1/nsenter.1.html
# nsenter --target 37834 --mount --uts --ipc --net --pid
# doing... 可以在容器里导入sql文件或者其他操作
# 退出容器 exit
```



##### 3. 创建django-blog容器

在django-blog目录下有三个文件，首先是Dockerfile，基础镜像是py3.6，里面运行的系统是ubuntu，我自己用的是git克隆将项目打包进镜像，也可以使用ADD命令添加。其次是sources.list，这个里存放的是阿里源。对于Dockerfile文件，需要注意的就是Django的settings里面指定的数据库，是后面创建django-blog容器时候link的mysql容器地址。`--link mysql:mysql` ，在django-blog容器里可以直接ping通，`ping mysql`

```dockerfile
# 基础镜像, 一个镜像Dockerfile必需的
FROM daocloud.io/python:3.6

# 维护者信息, 可以写邮箱网站啥的
MAINTAINER binbin <binloveplay1314@qq.com>

# ADD、COPY将当前目录里的文件拷贝到镜像中, ADD会自动解压
# 适用于自己有项目tar包里, 里面的配置信息例如settings都弄好了
# ADD blog.tar.gz /var/www

# 设置工作目录, 容器会自动cd到这里
WORKDIR /var/www

# 更新源，使用git下载blog项目, 或者可以自己ADD, /var/www/Django-blog/
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY sources.list /etc/apt
RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/enjoy-binbin/Django-blog.git

# 复制配置文件
RUN cp ./Django-blog/binblog/settings_docker.py ./Django-blog/binblog/settings.py

# 安装依赖, 使用阿里云镜像
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple/ -r ./Django-blog/requirements.txt --trusted-host mirrors.aliyun.com
RUN pip install --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com gunicorn

# 切换工作目录
WORKDIR /var/www/Django-blog

# 容器启动时执行的命令
CMD python manage.py makemigrations; python manage.py migrate; python manage.py create_fake_data; python manage.py collectstatic --noinput; python manage.py compress --force; gunicorn binblog.wsgi --bind 0.0.0.0:8000
```

下面是Django-blog的启动shell脚本，根据上面编写的Dockerfile生成镜像并且启动一个名django-blog容器。

```shell
#!/bin/bash
# 根据Dockfile创建镜像, 并且启动容器 by binbin

# 根据当前目录下的Dockerfile创建镜像
docker build -t bin/django-blog:v1 .

echo "---------Start django-blog image---------"
# 启动django-blog容器(先mysql、再django-blog、再nginx)
# --link 链接mysql容器, 注意容器的启动顺序 在容器里面可以ping mysql
# -v 挂载共享目录, 把项目代码共享出去给后面的nginx，nginx容器里可以看到有这个目录的，访问静态资源
# -p 端口映射, 容器内的8000映射到主机的8001
# -d 后台运行
# bin/django-blog:v1 镜像名
# 执行的命令 gunicorn安装后是在那里的
docker run --name django-blog \
--link mysql:mysql \
-v /var/www/Django-blog \
-p 8001:8000 \
-d bin/django-blog:v1
# -dit bin/django-blog:v1 /bin/bash

# 进行数据库迁移, 感觉可以多写一个sh文件用于执行, 或者写到dockfile里
# docker exec django-blog python manage.py makemigrations
# docker exec django-blog python manage.py migrate
# docker exec django-blog python manage.py create_fake_data
# docker exec django-blog python manage.py collectstatic --noinput
# docker exec django-blog python manage.py compress --force
# docker exec django-blog gunicorn binblog.wsgi --bind 0.0.0.0:8000 --daemon

echo "---------End django-blog image---------"
# 进入容器的方法 django-blog 容器名
# docker container inspect --format "{{.State.Pid}}" django-blog
# docker inspect --format "{{.State.Pid}}" django-blog
# 37834
#
# nsenter参数说明: http://man7.org/linux/man-pages/man1/nsenter.1.html
# nsenter --target 37834 --mount --uts --ipc --net --pid
# doing... 可以先自己在这里启动runserver看看是否通
# 退出容器 exit
```



##### 4. 启动Nginx容器

在nginx目录下有三个文件，一个是nginx的配置文件，另外两个就是Dockerfile和启动脚本了。这个基础镜像是nginx:1.14，里面的系统是Debian，所以配置文件存放的地方不同于Centos或Ubuntu。站点监听的是8000端口，容器可以进行端口映射，所以这里虽然是8000端口，但是我后面映射到主机的端口其实是80，静态文件是前面Django-blog容器共享出来的文件目录，`http://web:8000`是Django-blog容器的别名，在后面使用脚本创建容器的时link的。容器中link后可以相互ping通的，`ping web`

```nginx
server {
    listen         8000;  # 监听的端口，80端口，同时需要修改nginx默认的80页面
    server_name    www.binblog.cn;
    charset UTF-8;

    location /static{
        # 对标django-blog容器里共享出来的目录
        alias /var/www/Django-blog/collectedstatic;
    }
	
	location /media{
        # 对标django-blog容器里共享出来的目录
		alias /var/www/Django-blog/media;
	}

	location / {
        # 其他/下的就转发给django处理, docker中link后可以直接根据名称/别名访问容器
        proxy_pass http://web:8000;
	}
 }
```

对于Dockerfile文件，只是简单的将配置文件添加进去，并且以前台方式启动nginx服务。

```dockerfile
# 基础镜像
FROM daocloud.io/nginx:1.14

# 维护者
MAINTAINER binbin <binloveplay1314@qq.com>

# 这样创建并进入容器查看相关配置文件
# docker run -i -t  daocloud.io/nginx:1.14 /bin/bash

# 先删除里面的默认配置文件, 移入自己的配置
# 因为默认配置会占用80, 这个镜像是基于Debian, 所以配置文件信息是这样的
# RUN rm /etc/nginx/conf.d/default.conf
COPY binblog.conf /etc/nginx/conf.d/

# Run nginx
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
```

启动nginx容器的脚本文件，link到前面的django-web容器。

```shell
#!/bin/bash 
#
# build -t 根据dockerfile创建镜像 带标签
# 启动nginx容器(先mysql、再django-blog、再nginx)
# --link link到django-blog容器 django-blog:web 可以起别名web
# --volumes-from 共享django-blog容器里的项目目录
# -p 80:8000 这个8000是binblog.conf里nginx监听的端口, 映射到主机的80
# -p 8000:80 吧nginx默认的80映射到主机的8000, 访问可以看到nginx欢迎页
docker build -t bin/nginx:v1 .
#
echo "---------Start nginx image---------"
#
docker run --name nginx \
--link django-blog:web \
--volumes-from django-blog \
-p 80:8000 \
-p 8000:80 \
-d bin/nginx:v1
#
#
echo "---------End nginx image---------"
```



##### 最后就是总的启动脚本文件啦

```shell
#!/bin/bash
# 执行顺序 先mysql、然后web、最后nginx
# 删除所有None构建失败的镜像
# docker images | grep none | awk '{print $3}' | xargs docker rmi
# 删除本机所有容器
# docker ps -a | awk '{print $1}' | xargs docker rm -f

echo "start mysql ----------------"
cd mysql
source ./start_mysql.sh
sleep 2

echo "start django-blog ----------------"
cd ../django-blog
source ./start_django_blog.sh
sleep 2

echo "start nginx ----------------"
cd ../nginx
source ./start_nginx.sh

cd ..
```

