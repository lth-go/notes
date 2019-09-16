# Nginx 服务的基本配置

---

## 用于调试进程和定位问题的配置项

(1)是否以守护进程方式运行Nginx
语法: daemon on|off;
默认: daemon on;

(2)是否以master/worker方式工作
语法: master_process on|off;
默认: master_process on;

(3)error日志的设置
语法: error_logpathfile level;
默认: error_log logs/error.log error;

(4)是否处理几个特殊的调试点
语法: debug_points[stop|abort]

(5)仅对指定的客户端输出debug级别的日志
语法: debug_connection[IP|CIDR]

(6)限制coredump核心转储文件的大小
语法: worker_rlimit_core size;

(7)指定coredump文件生成目录
语法: working_directory path;

---

## 正常运行的配置项

(1)定义环境变量
语法: env VAR|VAR=VALUE

(2)嵌入其他配置文件
语法: includepathfile;

(3)pid文件的路径
语法: pid path/file;默认: pid logs/nginx.pid;

(4)Nginx worker进程运行的用户及用户组
语法: user username[groupname];
默认: user nobody nobody;

(5)指定Nginx worker进程可以打开的最大句柄描述符个数
语法: worker_rlimit_nofile limit;
设置一个worker进程可以打开的最大文件句柄数。

(6)限制信号队列
语法: worker_rlimit_sigpending limit;
设置每个用户发往Nginx的信号队列的大小。也就是说,当某个用户的信号队列满了,
这个用户再发送的信号量会被丢掉。

---

## 优化性能的配置项

(1)Nginx worker进程个数
语法: worker_processes number;
默认: worker_processes 1;

(2)绑定Nginx worker进程到指定的CPU内核
语法: worker_cpu_affinity cpumask[cpumask...]

(3)SSL硬件加速
语法: ssl_engine device;

(4)系统调用gettimeofday的执行频率
语法: timer_resolution t;

(5)Nginx worker进程优先级设置
语法: worker_priority nice;
默认: worker_priority 0;

---

## 事件类配置项

(1)是否打开accept锁
语法: accept_mutex[on|off]
默认: accept_mutext on;

(2)lock文件的路径
语法: lock_file path/file;
默认: lock_file logs/nginx.lock;

(3)使用accept锁后到真正建立连接之间的延迟时间
语法: accept_mutex_delay Nms;
默认: accept_mutex_delay 500ms;

(4)批量建立新连接
语法: multi_accept[on|off];
默认: multi_accept off;

(5)选择事件模型
语法: use[kqueue|rtsig|epoll|/dev/poll|select|poll|eventport];
默认: Nginx会自动使用最适合的事件模型。

(6)每个worker的最大连接数
语法: worker_connections number;

---

## 虚拟主机与请求的分发

(1)监听端口
语法: listen address:port[default(deprecated in 0.8.21)|default_server|[backlog=num|rcvbuf=size|sndbuf=size|accept_filter=filter|deferred|bind|ipv6only=[on|off]|ssl]]; 默
认: listen 80;
配置块: server

(2)主机名称
语法: server_name name[...];
默认: server_name"";
配置块: server

(3)server_names_hash_bucket_size
语法: server_names_hash_bucket_size size;
默认: server_names_hash_bucket_size 32|64|128;
配置块: http、server、location

(4)server_names_hash_max_size
语法: server_names_hash_max_size size;
默认: server_names_hash_max_size 512;
配置块: http、server、location

(5)重定向主机名称的处理
语法: server_name_in_redirect on|off;
默认: server_name_in_redirect on;
配置块: http、server或者location

(6)location
语法: location[=|~|~*|^~|@]/uri/{...}
配置块: server
1)=表示把URI作为字符串,以便与参数中的uri做完全匹配。
2)~表示匹配URI时是字母大小写敏感的。
3)~*表示匹配URI时忽略字母大小写问题。
4)^~表示匹配URI时只需要其前半部分与uri参数匹配即可。
5)@表示仅用于Nginx服务内部请求之间的重定向,带有@的location不直接处理用户请求。

## 文件路径的定义
(1)以root方式设置资源路径
语法: root path;
默认: root html;
配置块: http、server、location、if

(2)以alias方式设置资源路径
语法: alias path;
配置块: location

(3)访问首页
语法: index file...;
默认: index index.html;
配置块: http、server、location

(4)根据HTTP返回码重定向页面
语法: error_page code[code...][=|=answer-code]uri|@named_location
配置块: http、server、location、if

(5)是否允许递归使用error_page
语法: recursive_error_pages[on|off];
默认: recursive_error_pages off;
配置块: http、server、location

(6)try_files
语法: try_files path1[path2]uri;
配置块: server、location

---

## 内存及磁盘资源的分配

(1)HTTP包体只存储到磁盘文件中
语法: client_body_in_file_only on|clean|off;
默认: client_body_in_file_only off;
配置块: http、server、location

(2)HTTP包体尽量写入到一个内存buffer中
语法: client_body_in_single_buffer on|off;
默认: client_body_in_single_buffer off;
配置块: http、server、location

(3)存储HTTP头部的内存buffer大小
语法: client_header_buffer_size size;
默认: client_header_buffer_size 1k;
配置块: http、server

(4)存储超大HTTP头部的内存buffer大小
语法: large_client_header_buffers number size;
默认: large_client_header_buffers 48k;
配置块: http、server

(5)存储HTTP包体的内存buffer大小
语法: client_body_buffer_size size;
默认: client_body_buffer_size 8k/16k;配置块: http、server、location

(6)HTTP包体的临时存放目录
语法: client_body_temp_path dir-path[level1[level2[level3]]]
默认: client_body_temp_path client_body_temp;
配置块: http、server、location

(7)connection_pool_size
语法: connection_pool_size size;
默认: connection_pool_size 256;配置块: http、server

(8)request_pool_size
语法: request_pool_size size;
默认: request_pool_size 4k;
配置块: http、server

---

## 网络连接的设置

(1)读取HTTP头部的超时时间
语法: client_header_timeout time(默认单位:秒);默认: client_header_timeout 60;
配置块: http、server、location

(2)读取HTTP包体的超时时间
语法: client_body_timeout time(默认单位:秒);
默认: client_body_timeout 60;
配置块: http、server、location

(3)发送响应的超时时间
语法: send_timeout time;
默认: send_timeout 60;
配置块: http、server、location

(4)reset_timeout_connection语法: reset_timeout_connection on|off;
默认: reset_timeout_connection off;
配置块: http、server、location

(5)lingering_close
语法: lingering_close off|on|always;
默认: lingering_close on;
配置块: http、server、location

(6)lingering_time
语法: lingering_time time;
默认: lingering_time 30s;配置块: http、server、location

(7)lingering_timeout
语法: lingering_timeout time;
默认: lingering_timeout 5s;
配置块: http、server、location

(8)对某些浏览器禁用keepalive功能
语法: keepalive_disable[msie6|safari|none]...
默认: keepalive_disablemsie6 safari
配置块: http、server、location

(9)keepalive超时时间
语法: keepalive_timeout time(默认单位:秒);
默认: keepalive_timeout 75;
配置块: http、server、location

(10)一个keepalive长连接上允许承载的请求最大数
语法: keepalive_requests n;
默认: keepalive_requests 100;
配置块: http、server、location

(11)tcp_nodelay
语法: tcp_nodelay on|off;
默认: tcp_nodelay on;
配置块: http、server、location

(12)tcp_nopush
语法: tcp_nopush on|off;
默认: tcp_nopush off;
配置块: http、server、location

---

## MIME类型的设置

语法: type{...};
配置块: http、server、location

语法: default_type MIME-type;默认: default_type text/plain;
配置块: http、server、location

语法: types_hash_bucket_size size;
默认: types_hash_bucket_size 32|64|128;
配置块: http、server、location

语法: types_hash_max_size size;
默认: types_hash_max_size 1024;
配置块: http、server、location

---

## 对客户端请求的限制

语法: limit_except method...{...}
配置块: location

(2)HTTP请求包体的最大值
语法: client_max_body_size size;
默认: client_max_body_size 1m;
配置块: http、server、location

(3)对请求的限速
语法: limit_rate speed;
默认: limit_rate 0;
配置块: http、server、location、if

(4)limit_rate_after
语法: limit_rate_after time;
默认: limit_rate_after 1m;
配置块: http、server、location、if

---

## 文件操作的优化

(1)sendfile系统调用
语法: sendfile on|off;
默认: sendfile off;
配置块: http、server、location

(2)AIO系统调用
语法: aio on|off;
默认: aio off;
配置块: http、server、location

(3)directio
语法: directio size|off;
默认: directio off;
配置块: http、server、location

(4)directio_alignment
语法: directio_alignment size;
默认: directio_alignment 512;
配置块: http、server、location

(5)打开文件缓存
语法: open_file_cache max=N[inactive=time]|off;
默认: open_file_cache off;
配置块: http、server、location

(6)是否缓存打开文件错误的信息
语法: open_file_cache_errors on|off;
默认: open_file_cache_errors off;
配置块: http、server、location

(7)不被淘汰的最小访问次数
语法: open_file_cache_min_uses number;
默认: open_file_cache_min_uses 1;配置块: http、server、location

(8)检验缓存中元素有效性的频率
语法: open_file_cache_valid time;
默认: open_file_cache_valid 60s;
配置块: http、server、location

---

## 对客户端请求的特殊处理

(1)忽略不合法的HTTP头部
语法: ignore_invalid_headers on|off;
默认: ignore_invalid_headers on;
配置块: http、server

(2)HTTP头部是否允许下划线语法: underscores_in_headers on|off;
默认: underscores_in_headers off;
配置块: http、server

(3)对If-Modified-Since头部的处理策略
语法: if_modified_since[off|exact|before];
默认: if_modified_since exact;
配置块: http、server、location

(4)文件未找到时是否记录到error日志
语法: log_not_found on|off;
默认: log_not_found on;
配置块: http、server、location

(5)merge_slashes
语法: merge_slashes on|off;
默认: merge_slashes on;
配置块: http、server、location

(6)DNS解析地址
语法: resolver address...;
配置块: http、server、location

(7)DNS解析的超时时间
语法: resolver_timeout time;
默认: resolver_timeout 30s;
配置块: http、server、location

(8)返回错误页面时是否在Server中注明Nginx版本
语法: server_tokens on|off;
默认: server_tokens on;
配置块: http、server、location

－－－

##　ngx_http_core_module模块提供的变量

```
$arg_PARAMETER HTTP 请求中某个参数的值，如/index.php?site=www.ttlsa.com，可以用$arg_site取得www.ttlsa.com这个值.  
$args HTTP 请求中的完整参数。例如，在请求/index.php?width=400&height=200 中，$args表示字符串width=400&height=200.  
$binary_remote_addr 二进制格式的客户端地址。例如：\x0A\xE0B\x0E  
$body_bytes_sent 表示在向客户端发送的http响应中，包体部分的字节数  
$content_length 表示客户端请求头部中的Content-Length 字段  
$content_type 表示客户端请求头部中的Content-Type 字段  
$cookie_COOKIE 表示在客户端请求头部中的cookie 字段  
$document_root 表示当前请求所使用的root 配置项的值  
$uri 表示当前请求的URI，不带任何参数  
$document_uri 与$uri 含义相同  
$request_uri 表示客户端发来的原始请求URI，带完整的参数。$uri和$document_uri未必是用户的原始请求，在内部重定向后可能是重定向后的URI，而$request_uri 永远不会改变，始终是客户端的原始URI.  
$host 表示客户端请求头部中的Host字段。如果Host字段不存在，则以实际处理的server（虚拟主机）名称代替。如果Host字段中带有端口，如IP:PORT，那么$host是去掉端口的，它的值为IP。$host 是全小写的。这些特性与http_HEADER中的http_host不同，http_host只取出Host头部对应的值。
$hostname 表示 Nginx所在机器的名称，与 gethostbyname调用返回的值相同   
$http_HEADER 表示当前 HTTP请求中相应头部的值。HEADER名称全小写。例如，示请求中 Host头部对应的值 用 $http_host表   
$sent_http_HEADER 表示返回客户端的 HTTP响应中相应头部的值。HEADER名称全小写。例如，用 $sent_ http_content_type表示响应中 Content-Type头部对应的值   
$is_args 表示请求中的 URI是否带参数，如果带参数，$is_args值为 ?，如果不带参数，则是空字符串   
$limit_rate 表示当前连接的限速是多少，0表示无限速   
$nginx_version 表示当前 Nginx的版本号   
$query_string 请求 URI中的参数，与 $args相同，然而 $query_string是只读的不会改变   
$remote_addr 表示客户端的地址   
$remote_port 表示客户端连接使用的端口   
$remote_user 表示使用 Auth Basic Module时定义的用户名   
$request_filename 表示用户请求中的 URI经过 root或 alias转换后的文件路径   
$request_body 表示 HTTP请求中的包体，该参数只在 proxy_pass或 fastcgi_pass中有意义   
$request_body_file 表示 HTTP请求中的包体存储的临时文件名   
$request_completion 当请求已经全部完成时，其值为 “ok”。若没有完成，就要返回客户端，则其值为空字符串；或者在断点续传等情况下使用 HTTP range访问的并不是文件的最后一块，那么其值也是空字符串。  
$request_method 表示 HTTP请求的方法名，如 GET、PUT、POST等   
$scheme 表示 HTTP scheme，如在请求 https://nginx.com/中表示 https   
$server_addr 表示服务器地址   
$server_name 表示服务器名称   
$server_port 表示服务器端口   
$server_protocol 表示服务器向客户端发送响应的协议，如 HTTP/1.1或 HTTP/1.0  
```
