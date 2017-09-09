#time

time:
    time()
    float
    返回当前时间时间戳

clock:
    clock()
    float
    进程时间

sleep:
    sleep(seconds)
    None
    线程推迟指定的时间运行。单位为秒。

gmtime:
    gmtime(seconds=None)
    struct_time
    将一个时间戳转换为UTC时区的struct_time

localtime:
    localtime(seconds=None)
    struct_time
    将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。

mktime:
    mktime(struct_time)
    float
    将一个struct_time转化为时间戳。

strftime:
    strftime(format, struct_time=None)
    string
    把struct_time转化为格式化的时间字符串。

strptime:
    strptime(string, format)
    struct_time
    把一个格式化时间字符串转化为struct_time
