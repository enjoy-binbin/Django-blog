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