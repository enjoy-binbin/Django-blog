#!/bin/bash

# 启动mysql容器(先mysql、再django-blog、再nginx)
# --name mysql 启动后的容器名称
# -p 3307:3306 端口映射, 将mysql容器的3306端口映射到主机的3307(因为自己主机3306有个mysql)
# -e MYSQL_ROOT_PASSWORD=123456 配置的Mysql密码
# -v $PWD/conf:/etc/mysql/conf.d 将当前目录下的/conf文件夹挂在到容器里的/etc/mysql/conf.d, 如果自己有配置文件需要这样挂载
# -v $PWD/data:/var/lib/mysql 将当前目录下的data目录挂载到容器的 /var/lib/mysql, 还有其他文件也是同理
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
#
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
# 退出容器
# exit