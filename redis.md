# Redis

## Key:

###  SELECY db
选择数掘库

###  DEL key
该命令用于在 key 存在时删除 key。

###  EXISTS key
检查给定 key 是否存在。

###  TYPE key
返回 key 所储存的值的类型。

### RANDOMKEY
从当前数据库中随机返回一个 key 。

### DUMP key
序列化给定 key ，并返回被序列化的值。

### RENAME key newkey
修改 key 的名称
### RENAMENX key newkey
仅当 newkey 不存在时，将 key 改名为 newkey 。

### KEYS pattern
查找所有符合给定模式(pattern)的 key 。

### MOVE key db
将当前数据库的 key 移动到给定的数据库 db 当中。

### EXPIRE key seconds
为给定 key 设置过期时间。
### EXPIREAT key timestamp
为给定 key 设置过期时间。参数为UNIX 时间戳。
### PEXPIRE key milliseconds
设置 key 的过期时间以毫秒计。
### PEXPIREAT key milliseconds-timestamp
设置 key 过期时间的时间戳(unix timestamp)。
### TTL key
以秒为单位，返回给定 key 的剩余生存时间(TTL, time to live)。
### PTTL key
以毫秒为单位返回 key 的剩余的过期时间。
### PERSIST key
移除 key 的过期时间，key 将持久保持。

***

## String

### SET key value
设置指定 key 的值
### SETNX key value
只有在 key 不存在时设置 key 的值。
### GETSET key value
将给定 key 的值设为 value ，并返回 key 的旧值(old value)。
### MSET key value [key value ...]
同时设置一个或多个 key-value 对。
### MSETNX key value [key value ...]
同时设置一个或多个 key-value 对，当且仅当所有给定 key 都不存在。

### GET key
获取指定 key 的值。
### MGET key1 [key2..]
获取所有(一个或多个)给定 key 的值。
### GETRANGE key start end
返回 key 中字符串值的子字符
### STRLEN key
返回 key 所储存的字符串值的长度。

### GETBIT key offset
对 key 所储存的字符串值，获取指定偏移量上的位(bit)。
### SETBIT key offset value
对 key 所储存的字符串值，设置或清除指定偏移量上的位(bit)。

### SETEX key seconds value
将值 value 关联到 key ，并将 key 的过期时间设为 seconds (以秒为单位)。
### PSETEX key milliseconds value
将值 value 关联到 key ，并将 key 的过期时间设为 seconds (以毫秒为单位)。

### INCR key
将 key 中储存的数字值增一。
### INCRBY key increment
将 key 所储存的值加上给定的增量值（increment）。
### INCRBYFLOAT key increment
将 key 所储存的值加上给定的浮点增量值（increment）。
### DECR key
将 key 中储存的数字值减一。
### DECRBY key decrement
key 所储存的值减去给定的减量值（decrement） 。

### APPEND key value
如果 key 已经存在并且是一个字符串， APPEND 命令将 value 追加到 key 原来的值的末尾。
### SETRANGE key offset value
用 value 参数覆写给定 key 所储存的字符串值，从偏移量 offset 开始。

***

## Hash

### HSET key field value
将哈希表 key 中的字段 field 的值设为 value 。
### HMSET key field1 value1 [field2 value2 ]
同时将多个 field-value (域-值)对设置到哈希表 key 中。
### HSETNX key field value
只有在字段 field 不存在时，设置哈希表字段的值。

### HKEYS key
获取所有哈希表中的字段
### HVALS key
获取哈希表中所有值
### HGET key field
获取存储在哈希表中指定字段的值。
### HMGET key field1 [field2]
获取所有给定字段的值
### HGETALL key
获取在哈希表中指定 key 的所有字段和值
### HSCAN key cursor [MATCH pattern] [COUNT count]
迭代哈希表中的键值对。
### HEXISTS key field
查看哈希表 key 中，指定的字段是否存在。
### HLEN key
获取哈希表中字段的数量

### HDEL key field2 [field2]
删除一个或多个哈希表字段

### HINCRBY key field increment
为哈希表 key 中的指定字段的整数值加上增量 increment 。
### HINCRBYFLOAT key field increment
为哈希表 key 中的指定字段的浮点数值加上增量 increment 。

***

## List

### RPUSH key value1 [value2]
在列表中添加一个或多个值
### RPUSHX key value
为已存在的列表添加值
### LPUSH key value1 [value2]
将一个或多个值插入到列表头部
### LPUSHX key value
将一个或多个值插入到已存在的列表头部
### LINSERT key BEFORE|AFTER pivot value
在列表的元素前或者后插入元素
### LSET key index value
通过索引设置列表元素的值

### LLEN key
获取列表长度
### LINDEX key index
通过索引获取列表中的元素
### LRANGE key start stop
获取列表指定范围内的元素

### LPOP key
移出并获取列表的第一个元素
### RPOP key
移除并获取列表最后一个元素
### BLPOP key1 [key2 ] timeout
移出并获取列表的第一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。
### BRPOP key1 [key2 ] timeout
移出并获取列表的最后一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。
### BRPOPLPUSH source destination timeout
从列表中弹出一个值，将弹出的元素插入到另外一个列表中并返回它； 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。
### RPOPLPUSH source destination
移除列表的最后一个元素，并将该元素添加到另一个列表并返回
### LTRIM key start stop
对一个列表进行修剪(trim)，就是说，让列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除。
### LREM key count value
移除相应数量的列表元素

***

## Set

### SADD key member1 [member2]
向集合添加一个或多个成员

### SMEMBERS key
返回集合中的所有成员
### SRANDMEMBER key [count]
返回集合中一个或多个随机数
### SCARD key
获取集合的成员数
### SISMEMBER key member
判断 member 元素是否是集合 key 的成员
### SSCAN key cursor [MATCH pattern] [COUNT count]
迭代集合中的元素

### SMOVE source destination member
将 member 元素从 source 集合移动到 destination 集合

### SPOP key
移除并返回集合中的一个随机元素
### SREM key member1 [member2]
移除集合中一个或多个成员

### SDIFF key1 [key2]
返回给定所有集合的差集
### SDIFFSTORE destination key1 [key2]
返回给定所有集合的差集并存储在 destination 中
### SINTER key1 [key2]
返回给定所有集合的交集
### SINTERSTORE destination key1 [key2]
返回给定所有集合的交集并存储在 destination 中
### SUNION key1 [key2]
返回所有给定集合的并集
### SUNIONSTORE destination key1 [key2]
所有给定集合的并集存储在 destination 集合中

***

## Sorted Set

### ZADD key score1 member1 [score2 member2]
向有序集合添加一个或多个成员，或者更新已存在成员的分数

### ZREVRANK key member
返回有序集合中指定成员的排名
### ZSCORE key member
返回有序集中，成员的分数值
### ZRANK key member
返回有序集合中指定成员的索引

### ZCARD key
获取有序集合的成员数
### ZCOUNT key min max
计算在有序集合中指定区间分数的成员数
### ZSCAN key cursor [MATCH pattern] [COUNT count]
迭代有序集合中的元素（包括元素成员和元素分值）
### ZLEXCOUNT key min max
在有序集合中计算指定字典区间内成员数量

### ZRANGE key start stop [WITHSCORES]
通过索引区间返回有序集合成指定区间内的成员
### ZRANGEBYLEX key min max [LIMIT offset count]
通过字典区间返回有序集合的成员
### ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT]
通过分数返回有序集合指定区间内的成员

### ZREVRANGE key start stop [WITHSCORES]
返回有序集中指定区间内的成员，通过索引，分数从高到低
### ZREVRANGEBYSCORE key max min [WITHSCORES]
返回有序集中指定分数区间内的成员，分数从高到低排序

### ZINCRBY key increment member
有序集合中对指定成员的分数加上增量 increment

### ZINTERSTORE destination numkeys key [key ...]
计算给定的一个或多个有序集的交集并将结果集存储在新的有序集合 key 中
### ZUNIONSTORE destination numkeys key [key ...]
计算给定的一个或多个有序集的并集，并存储在新的 key 中

### ZREM key member [member ...]
移除有序集合中的一个或多个成员
### ZREMRANGEBYLEX key min max
移除有序集合中给定的字典区间的所有成员
### ZREMRANGEBYRANK key start stop
移除有序集合中给定的排名区间的所有成员
### ZREMRANGEBYSCORE key min max
移除有序集合中给定的分数区间的所有成员

***

## Pub/Sub

### SUBSCRIBE channel [channel ...]
订阅给定的一个或多个频道的信息。
### PSUBSCRIBE pattern [pattern ...]
订阅一个或多个符合给定模式的频道。

### UNSUBSCRIBE [channel [channel ...]]
指退订给定的频道。
### PUNSUBSCRIBE [pattern [pattern ...]]
退订所有给定模式的频道。

### PUBLISH channel message
将信息发送到指定的频道。

### PUBSUB subcommand [argument [argument ...]]
查看订阅与发布系统状态。

***

##Transaction

### MULTI
标记一个事务块的开始。
### EXEC
执行所有事务块内的命令。
### DISCARD
取消事务，放弃执行事务块内的所有命令。

### UNWATCH
取消 WATCH 命令对所有 key 的监视。
### WATCH key [key ...]
监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。

***

##Config

1. Redis默认不是以守护进程的方式运行，可以通过该配置项修改，使用yes启用守护进程
`daemonize no`

2. 当Redis以守护进程方式运行时，Redis默认会把pid写入/var/run/redis.pid文件，可以通过pidfile指定
`pidfile /var/run/redis.pid`

3. 指定Redis监听端口，默认端口为6379
`port 6379`

4. 绑定的主机地址
`bind 127.0.0.1`

5. 当客户端闲置多长时间后关闭连接，如果指定为0，表示关闭该功能
`timeout 300`

6. 指定日志记录级别，Redis总共支持四个级别：debug、verbose、notice、warning，默认为verbose
`loglevel verbose`

7. 日志记录方式，默认为标准输出，如果配置Redis为守护进程方式运行，而这里又配置为日志记录方式为标准输出，则日志将会发送给/dev/null
`logfile stdout`

8. 设置数据库的数量，默认数据库为0，可以使用SELECT <dbid>命令在连接上指定数据库id
`databases 16`

9. 指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合
`save <seconds> <changes>`

10. 指定存储至本地数据库时是否压缩数据，默认为yes，Redis采用LZF压缩，如果为了节省CPU时间，可以关闭该选项，但会导致数据库文件变的巨大

`rdbcompression yes`

11. 指定本地数据库文件名，默认值为dump.rdb

`dbfilename dump.rdb`

12. 指定本地数据库存放目录

`dir ./`

13. 设置当本机为slav服务时，设置master服务的IP地址及端口，在Redis启动时，它会自动从master进行数据同步

`slaveof <masterip> <masterport>`

14. 当master服务设置了密码保护时，slav服务连接master的密码

`masterauth <master-password>`

15. 设置Redis连接密码，如果配置了连接密码，客户端在连接Redis时需要通过AUTH <password>命令提供密码，默认关闭

`requirepass foobared`

16. 设置同一时间最大客户端连接数，默认无限制，Redis可以同时打开的客户端连接数为Redis进程可以打开的最大文件描述符数，如果设置 maxclients 0，表示不作限制。当客户端连接数到达限制时，Redis会关闭新的连接并向客户端返回max number of clients reached错误信息

`maxclients 128`

17. 指定Redis最大内存限制，Redis在启动时会把数据加载到内存中，达到最大内存后，Redis会先尝试清除已到期或即将到期的Key，当此方法处理 后，仍然到达最大内存设置，将无法再进行写入操作，但仍然可以进行读取操作。Redis新的vm机制，会把Key存放内存，Value会存放在swap区

`maxmemory <bytes>`

18. 指定是否在每次更新操作后进行日志记录，Redis在默认情况下是异步的把数据写入磁盘，如果不开启，可能会在断电时导致一段时间内的数据丢失。因为 redis本身同步数据文件是按上面save条件来同步的，所以有的数据会在一段时间内只存在于内存中。默认为no

`appendonly no`

19. 指定更新日志文件名，默认为appendonly.aof

`appendfilename appendonly.aof`

20. 指定更新日志条件，共有3个可选值：
```
no：表示等操作系统进行数据缓存同步到磁盘（快）
always：表示每次更新操作后手动调用fsync()将数据写到磁盘（慢，安全）
everysec：表示每秒同步一次（折衷，默认值）

appendfsync everysec
```

21. 指定是否启用虚拟内存机制，默认值为no，简单的介绍一下，VM机制将数据分页存放，由Redis将访问量较少的页即冷数据swap到磁盘上，访问多的页面由磁盘自动换出到内存中（在后面的文章我会仔细分析Redis的VM机制）
`vm-enabled no`

22. 虚拟内存文件路径，默认值为/tmp/redis.swap，不可多个Redis实例共享
`vm-swap-file /tmp/redis.swap`

23. 将所有大于vm-max-memory的数据存入虚拟内存,无论vm-max-memory设置多小,所有索引数据都是内存存储的(Redis的索引数据 就是keys),也就是说,当vm-max-memory设置为0的时候,其实是所有value都存在于磁盘。默认值为0
`vm-max-memory 0`

24. Redis swap文件分成了很多的page，一个对象可以保存在多个page上面，但一个page上不能被多个对象共享，vm-page-size是要根据存储的 数据大小来设定的，作者建议如果存储很多小对象，page大小最好设置为32或者64bytes；如果存储很大大对象，则可以使用更大的page，如果不 确定，就使用默认值
`vm-page-size 32`

25. 设置swap文件中的page数量，由于页表（一种表示页面空闲或使用的bitmap）是在放在内存中的，，在磁盘上每8个pages将消耗1byte的内存。
`vm-pages 134217728`

26. 设置访问swap文件的线程数,最好不要超过机器的核数,如果设置为0,那么所有对swap文件的操作都是串行的，可能会造成比较长时间的延迟。默认值为4
`vm-max-threads 4`

27. 设置在向客户端应答时，是否把较小的包合并为一个包发送，默认为开启
`glueoutputbuf yes`

28. 指定在超过一定的数量或者最大的元素超过某一临界值时，采用一种特殊的哈希算法
```
hash-max-zipmap-entries 64
hash-max-zipmap-value 512
```

29. 指定是否激活重置哈希，默认为开启（后面在介绍Redis的哈希算法时具体介绍）
`activerehashing yes`

30. 指定包含其它的配置文件，可以在同一主机上多个Redis实例之间使用同一份配置文件，而同时各个实例又拥有自己的特定配置文件
`include /path/to/local.conf`
