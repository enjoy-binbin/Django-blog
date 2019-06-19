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