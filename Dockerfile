# 基础镜像, 一个镜像Dockerfile必需的
FROM daocloud.io/python:3.6

# 维护者信息, 可以写邮箱网站啥的
MAINTAINER binbin <binloveplay1314@qq.com>

ADD . /app
WORKDIR /app

# 安装依赖,
RUN pip install --no-cache-dir -i https://pypi.douban.com/simple -r ./requirements.txt --trusted-host mirrors.aliyun.com