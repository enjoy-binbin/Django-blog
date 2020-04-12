filebeat_nginx.yml:
    收集简单nginx的访问日志, 记录只是单纯的message信息, 索引名固定

filebeat_nginx_json.yml
    收集nginx的访问日志, 以json格式输出, 自定义索引名
    1. 修改nginx日志格式
        nginx日志参考: http://nginx.org/en/docs/http/ngx_http_log_module.html#log_format
    2. 设置配置文件 output->es:
        https://www.elastic.co/guide/en/beats/filebeat/7.6/elasticsearch-output.html
        https://www.elastic.co/guide/en/beats/filebeat/7.6/configuration-template.html
        # 有个坑, 需要多配置
        # A hole: https://www.elastic.co/guide/en/beats/filebeat/current/ilm.html
        setup.ilm.enabled: false
        
filebeat_nginx_json_error.yml
    使用tags打标签收集access和error日志
    
  
filebeat_redis.yml
    将数据存入reids, 之后需用logstash 根据tags标签区分, 多种数据可以只存入一个redis key里
    https://www.elastic.co/guide/en/beats/filebeat/7.6/redis-output.html