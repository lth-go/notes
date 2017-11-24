# 系统管理

## X-Windows

### xinit
是Linux下X-Window系统的初始化程序
### startx
用来启动X Window

## 日志

### journalctl
systemd日志管理

## 时间

### timedatectl
systemd时间管理

### date
显示或设置系统时间与日期
### ntpdate
使用网络计时协议（NTP）设置日期和时间
### tzselect
设置时区

## 系统关机和重启

### sync
用于强制被改变的内容立刻写入磁盘

### shutdown
用来执行系统关机的命令
### reboot
重新启动正在运行的Linux操作系统

## 进程

### systemctl
systemd系统服务管理器指令

### init
init进程是所有Linux进程的父进程

### ps
报告当前系统的进程状态
### pstree
以树状图的方式展现进程之间的派生关系

### kill
删除执行中的程序或工作
### killall
使用进程的名称来杀死一组进程

### nice
改变程序执行的优先权等级
### renice
修改正在运行的进程的调度优先级

### ipcs
分析消息队列共享内存和信号量
### ipcrm
删除消息队列、信号集、或者共享内存标识

### pmap
报告进程的内存映射关系

## 性能监测

### dstat
实时监控

### sar
监控

### lsof
显示Linux系统当前已打开的所有文件列表

### free
显示内存的使用情况

### top / htop
显示或管理执行中的程序

### watch
周期性的方式执行给定的指令

### vmstat
显示虚拟内存状态

### iostat
io监控

### tcpdump
tcp抓包

### time
统计给定命令所花费的总时间

## 作业管理

### jobs
显示Linux中的任务列表及任务状态
### fg
将后台作业放到前台终端运行
### bg
用于将作业放到后台运行

### crontab
提交和管理用户的需要周期性执行的任务

### at
在指定时间执行一个任务
### atq
列出当前用户的at任务列表
### atrm
删除待执行任务队列中的指定任务

### nohup
将程序以忽略挂起信号的方式运行起来

### disown
从jobs中移除

## 用户和工作组管理

### su
用于切换当前用户身份到其他用户身份

### sudo
以其他身份来执行命令

### id
显示用户的ID以及所属群组的ID

### groups
用来打印指定用户所属的工作组

### last
用户登录记录

### lastlog
显示系统中所有用户最近一次登录信息

### chsh
用来更换登录系统时使用的shell

### passwd
用于让用户可以更改自己的密码

### usermod
用于修改用户的基本信息
### useradd
创建的新的系统用户
### userdel
用于删除给定的用户以及与用户相关的文件

### groupmod
更改群组识别码或名称
### groupadd
用于创建一个新的工作组
### groupdel
用于删除指定的工作组

## 文件系统管理

### du
显示每个文件和目录的磁盘使用空间
### df
显示磁盘的相关信息

### dumpe2fs
用于打印“ext2/ext3”文件系统的超级块和快组信息

### mke2fs
创建磁盘分区上的“etc2/etc3”文件系统

### fdisk
查看磁盘使用情况和磁盘分区

### parted
磁盘分区和分区大小调整工具

### mknod
创建字符设备文件和块设备文件

### partprobe
不重启的情况下重读分区

### badblocks
查找磁盘中损坏的区块

### mkfs
用于在设备上创建Linux文件系统

### e2label
设置第二扩展文件系统的卷标

### fsck
检查并且试图修复文件系统中的错误

### ln
用来为文件创件连接

### mount
用于加载文件系统到指定的加载点
### umount
用于卸载已经加载的文件系统

### mkswap
建立和设置SWAP交换分区
### swapon
激活Linux系统中交换空间
### swapoff
关闭指定的交换空间

## 高级文件系统管理

### quota
显示磁盘已使用的空间与限制
### quotastats
显示系统当前的磁盘配额运行状态信息
### edquota
用于编辑指定用户或工作组磁盘配额
### quotaon
激活Linux内核中指定文件系统的磁盘配额功能
### quotacheck
检查磁盘的使用空间与限制
### quotaoff
关闭Linux内核中指定文件系统的磁盘配额功能
### repquota
报表的格式输出磁盘空间限制的状态

### lvcreate
用于创建LVM的逻辑卷
### lvscan
扫描逻辑卷
### lvdisplay
显示逻辑卷属性
### lvextend
扩展逻辑卷空间
### lvreduce
收缩逻辑卷空间
### lvremove
删除指定LVM逻辑卷
### lvresize
调整逻辑卷空间大小

### pvscan
扫描系统中所有硬盘的物理卷列表
### pvcreate
将物理硬盘分区初始化为物理卷
### pvdisplay
显示物理卷的属性
### pvremove
删除一个存在的物理卷

### vgcreate
用于创建LVM卷组
### vgscan
扫描并显示系统中的卷组
### vgdisplay
显示LVM卷组的信息
### vgextend
向卷组中添加物理卷
### vgreduce
从卷组中删除物理卷
### vgchange
修改卷组属性
### vgremove
用于用户删除LVM卷组

----------

# 文件目录管理

## 目录基本操作

### ls
显示目录内容列表
### tree
树状图列出目录的内容

### cd
切换用户当前工作目录

### pwd
绝对路径方式显示用户当前工作目录

### cp
将源文件或目录复制到目标文件或目录中
### mv
用来对文件或目录重新命名

### mkdir
用来创建目录

### rm
用于删除给定的文件和目录

## 文件查找

### locate
查找文件或目录

### which
查找并显示给定命令的绝对路径

### find
在指定目录下查找文件

### whereis
查找二进制程序、代码等相关文件路径

## 文件内容查看

### cat
连接文件并打印到标准输出设备上

### head
在屏幕上显示指定文件的开头若干行
### tail
在屏幕上显示指定文件的末尾若干行

### less
分屏上下翻页浏览文件内容

### hexdump
显示文件十六进制格式
### od
输出文件的八进制、十六进制等格式编码的字节

### diff
比较给定的两个文件的不同

## 文件权限属性设置

### setfacl
设置文件访问控制列表

### umask
用来设置限制新建文件权限的掩码

### chattr
用来改变文件属性
### lsattr
查看文件的第二扩展文件系统属性

### chmod
用来变更文件或目录的权限
### chown
用来变更文件或目录的拥有者或所属群组
### chgrp
用来变更文件或目录的所属群组

### stat
用于显示文件的状态信息
### file
用来探测给定文件的类型。

## 文本处理

### touch
创建新的空文件

### xargs
给其他命令传递参数的一个过滤器

### grep
强大的文本搜索工具

### paste
将多个文件按列队列合并
### sort
将文件进行排序并输出
### tee
把数据重定向到给定文件和屏幕上
### tr
将字符进行替换压缩和删除
### uniq
报告或忽略文件中的重复行
### wc
统计文件的字节数、字数、行数

### awk
文本和数据进行处理的编程语言
### sed
功能强大的流式文本编辑器

## 文件编码处理

### iconv
转换文件的编码方式
### convmv
转换文件夹的编码方式

### dos2unix
将DOS格式文本文件转换成Unix格式
### unix2dos
将Unix格式文本文件转换成DOS格式

### dd
复制文件并对原文件的内容进行转换和格式化处理

## 文件压缩与解压

### tar
Linux下的归档使用工具，用来打包和备份。

### zip
可以用来解压缩文件
### unzip
用于解压缩由zip命令压缩的压缩包

### zipsplit
将较大的zip压缩包分割成各个较小的压缩包

### zipinfo
用来列出压缩文件信息

### unar
解压缩文件并转码

----------

# 网络管理

## 网络应用

### axel
多线程下载工具

### curl
利用URL规则在命令行下工作的文件传输工具

### ftp
因特网文件传输程序

### wget
非交互式网络下载器

### ssh
OpenSSH SSH 客户端

### ssh-keygen
为ssh生成、管理和转换认证密钥

### scp
加密的方式在本地主机和远程主机之间复制文件

### sshfs
共享远程文件夹

## 高级网络

### iptables
防火墙软件
### iptstate
显示iptables的工作状态

## 网络测试

### dig
域名查询工具
### host
常用的分析域名查询工具

### ping
发送ICMP报文到指定主机
### traceroute
打印到一台网络主机的路由数据包

### netstat / ss
查看网络连接状况

### nc
建立链接并返回两个数据流

## 网络配置

### nmcli
NetworkManager客户端

### ifconfig / ip
配置和显示系统网卡的网络参数

### ifup
激活指定的网络接口
### ifdown
禁用指定的网络接口

### route
显示并设置Linux中静态路由表

----------

# 工具

## 常用命令

### cal
显示当前日历或指定日期的日历

### clear
清除当前屏幕终端上的任何信息

### sleep
将目前动作延迟一段时间

### md5sum
计算和校验文件报文摘要的工具程序

### man
查看Linux中的指令帮助

## 软件包管理

### rpm
RPM软件包的管理工具

### yum
基于RPM的软件包管理器
### dnf
新一代的RPM软件包管理器

### patch
为开放源代码软件安装补丁程序

## 编程开发

### gcc
基于C/C++的编译器
### gdb
功能强大的程序调试器
### make
GNU的工程化编译工具

### readelf
用于显示elf格式文件的信息

### objdump
显示二进制文件信息
### pstack
显示每个进程的栈跟踪
### nm
显示二进制目标文件的符号表

### ld
将目标文件连接为可执行程序
### ldd
打印程序或者库文件所依赖的共享库列表
### ldconfig
动态链接库管理命令

## Shell

### sh
shell命令解释器

### exec
调用并执行指定的命令

### exit
退出当前的shell

### history
用于显示历史命令

### source
引入变量

### export
设置或显示系统环境变量
### env
显示系统中已存在的环境变量
### declare
声明或显示shell变量
### set
显示或设置shell特性及shell变量
### unset
删除指定的shell变量或函数

### read
从键盘读取变量值
### readonly
定义只读shell变量或函数

### echo
输出指定的字符串或者变量

### type
显示指定命令的类型

### alias
用来设置指令的别名
### unalias
删除由alias设置的别名

### let
简单的计算器
### expr
表达式计算工具

### test
shell环境中测试条件表达式工具

### mktemp
创建临时文件供shell脚本使用

### shift
移动参数

----------

# 硬件 | 内核

## 内核与模块管理

### chroot
把根目录换成指定的目的目录

### uname
显示Linux系统信息
### lsb_release
显示发行版本信息
### dmesg
显示Linux系统启动信息

### mkinitrd
建立要载入ramdisk的映像文件

### modprobe
自动处理可载入模块
### lsmod
显示已载入系统的模块
### insmod
将给定的模块加载到内核中
### rmmod
从运行的内核中移除指定的内核模块

## 硬件管理

### lspci
显示当前主机的所有PCI总线信息
### lsusb
显示本机的USB设备列表信息
### arch
显示当前主机的硬件架构类型
