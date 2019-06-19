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