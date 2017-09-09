#os

**操作系统相关函数**

os.environ 
    一个dictionary 包含环境变量的映射关系 os.environ["HOME"] 可以得到环境变量HOME的值 
os.chdir(dir) 
    改变当前目录 os.chdir('d:\\outlook') 注意windows下用到转义 
os.getcwd() 
    得到当前目录 
os.getegid() 
    得到有效组id  os.getgid() 得到组id 
os.getuid() 
    得到用户id  
os.geteuid() 
	得到有效用户id 
os.setegid() 
    设置gid
os.seteuid()
    设置uid
os.getgruops() 
    得到用户组名称列表 
os.getlogin() 
    得到用户登录名称 
os.getenv 
    得到环境变量 
os.putenv 
    设置环境变量 
os.umask 
    设置umask 
os.system(cmd) 
    利用系统调用，运行cmd命令 

##常用路径名操作

os.path.abspath(path)
    返回路径名path的规范化的绝对路径。

os.path.basename(path)
    返回路径名path的主文档名。

os.path.commonprefix(list)
    返回list中所有路径的最长通用前缀（逐字符比较）。

os.path.dirname(path)
    返回路径名path的目录名。在path上调用函数split()，返回的二元组中的第一个元素就是目录名。

os.path.exists(path)
    如果path引用一个存在的路径，返回True。如果path引用一个断开的符号链接，返回False。

os.path.lexists(path)
    如果path引用一个存在的路径，返回True。对于断开的符号链接也返回True。

os.path.expanduser(path)
    在Unix和Windows平台上，返回参数，参数中开头的~或者~user被替换成user的主／家目录。

os.path.expandvars(path)
    返回参数，其中的环境变量被扩展。

os.path.getatime(path)
    返回path的最后访问时间。

os.path.getmtime(path)
    返回path的最后修改时间。

os.path.getctime(path)
    返回系统的ctime，在Unix这样的系统上，它是文件元数据最后修改时间（或者可以说是文件状态最后修改时间）

os.path.getsize(path)
    返回path的大小，以字节为单位。如果文件不存在或者不可访问，返回os.error。

os.path.isabs(path)
    如果path是绝对路径名，返回True。

os.path.isfile(path)
    如果path是一个存在的普通文件，返回True。

os.path.isdir(path)
    如果path是一个存在的目录，返回True。

os.path.islink(path)
    如果path引用的目录条目是个符号链接，返回True。

os.path.ismount(path)
    如果路径名path是一个mount point（挂载点），返回True。

os.path.join(path1[, path2[, ...]])
    将一个或多个路径正确地连接起来。

os.path.normcase(path)
    标准化路径名的大小写。

os.path.normpath(path)
    标准化路径名，合并多余的分隔符和上层引用，这样A//B, A/B/, A/./B 和A/foo/../B 都变成 A/B。

os.path.realpath(path)
    返回指定的文件名的规范名字，并消除路径中遇到的任何符号链接（如果操作系统支持的话）。

os.path.relpath(path[, start])
    返回自当前目录或者可选的start 目录的 path相对文件路径。start 默认为os.curdir。

os.path.samefile(path1, path2)
    如果两个路径名参数引用的是相同的文件或目录（由设备号和i-node号指示），则返回True。

os.path.sameopenfile(fp1, fp2)
    如果描述符fp1 和fp2引用的是相同的文件，则返回True。

os.path.samestat(stat1, stat2)
    如果文件信息元组stat1和stat2引用的是相同的文件，则返回True。

os.path.split(path)
    将路径名path 分割成(head, tail)，其中tail路径名的最后一部分，head 是其之前的所有部分。

os.path.splitdrive(path)
    将path分割成一个(drive, tail)对，其中drive是一个驱动器描述符或者空字符串。

os.path.splitext(path)
    将路径名path分割成一个(root, ext)对使得root + ext == path，ext 为空或者以点号开始并至多包含一个点。

os.path.splitunc(path)
    将 path 分隔成一个(unc, rest)对，unc 是UNC挂载点（例如r'\\hostmount'），rest 是路径剩下的部分（例如 r'\path\file.ext'）。

os.path.supports_unicode_filenames
    如果可以使用任意Unicode 字符串作为文件名则为True（在文件系统强加的限制之内）。
