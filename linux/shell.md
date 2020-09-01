# Shell

## Shell变量

### 变量名命名规则

* 首个字符必须为字母
* 中间不能有空格
* 不能使用标点符号
* 不能使用bash里的关键字

**除了显式地直接赋值,还可以用语句给变量赋值**

```
# 将 /etc 下目录的文件名循环出来
for file in `ls /etc`
```

---

### 使用变量

$ 使用定义过的变量

```
your_name="test"
echo $your_name
echo ${your_name}
```

### 只读变量

使用 readonly 命令可以将变量定义为只读变量,只读变量的值不能被改变

```
readonly variable_name
```

### 删除变量

使用 unset 命令可以删除变量,(不能删除只读命令)

```
unset variable_name
```

### 变量类型

运行shell时,会同时存在三种变量：

1. 局部变量 局部变量在脚本或命令中定义,仅在当前shell实例中有效,其他shell启动的程序不能访问局部变量。
2. 环境变量 所有的程序,包括shell启动的程序,都能访问环境变量,有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
3. shell变量 shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量,有一部分是局部变量,这些变量保证了shell的正常运行

---

## Shell 字符串

字符串是shell编程中最常用最有用的数据类型（除了数字和字符串,也没啥其它类型好用了）,字符串可以用单引号,也可以用双引号,也可以不用引号。单双引号的区别跟PHP类似。

### 单引号

str='this is a string'

单引号字符串的限制：

    单引号里的任何字符都会原样输出,单引号字符串中的变量是无效的；
    单引号字串中不能出现单引号（对单引号使用转义符后也不行）。

### 双引号

your_name='qinjx'
str="Hello, I know your are \"$your_name\"! \n"

双引号的优点：

    双引号里可以有变量
    双引号里可以出现转义字符

### 拼接字符串

your_name="qinjx"
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting $greeting_1

### 获取字符串长度

string="abcd"
echo ${#string} #输出 4

### 提取子字符串

以下实例从字符串第 2 个字符开始截取 4 个字符：

string="runoob is a great site"
echo ${string:1:4} # 输出 unoo

### 查找子字符串

查找字符 "i 或 s" 的位置：

string="runoob is a great company"
echo `expr index "$string" is`  # 输出 8

---

## Shell 注释

以"#"开头的行就是注释,会被解释器忽略

---

## Shell 传递参数

|参数处理|说明|
|---|---|
|`$0` | 文件名|
|`$n` | 第n个参数|
|`$#` | 传递到脚本的参数个数|
|`$*` | 以一个单字符串显示所有向脚本传递的参数|
|`$$` | 脚本运行的当前进程ID号|
|`$!` | 后台运行的最后一个进程的ID号|
|`$@` | 与`$*`相同，但是使用时加引号，并在引号中返回每个参数|
|`$-` | 显示Shell使用的当前选项，与set命令功能相同|
|`$?` | 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误|

```
$* 与 $@ 区别：

相同点：都是引用所有参数。
不同点：只有在双引号中体现出来。假设在脚本运行时写了三个参数 1、2、3，，则 " * " 等价于 "1 2 3"（传递了一个参数），而 "@" 等价于 "1" "2" "3"（传递了三个参数）。
```
---

## Shell 数组

### 数组定义

Shell 数组用括号来表示,元素用"空格"符号分割开

```
array_name=(value1 ... valuen)
```

### 下标定义数组

```
array_name[0]=value0
array_name[1]=value1
array_name[2]=value2
```

### 读取数组

```
${array_name[index]}
```

### 获取数组中的所有元素

使用@ 或 * 可以获取数组中的所有元素

```
my_array[0]=A
my_array[1]=B
my_array[2]=C
my_array[3]=D

echo "数组的元素为: ${my_array[*]}"
echo "数组的元素为: ${my_array[@]}"
```

### 获取数组的长度

获取数组长度的方法与获取字符串长度的方法相同

```
my_array[0]=A
my_array[1]=B
my_array[2]=C
my_array[3]=D

echo "数组元素个数为: ${#my_array[*]}"
echo "数组元素个数为: ${#my_array[@]}"
```

---

## Shell 基本运算符

### Shell 支持的运算符

* 算数运算符
* 关系运算符
* 布尔运算符
* 字符串运算符
* 文件测试运算符

原生bash不支持简单的数学运算，可以通过$((  ))实现

```
val=`expr 2 + 2`
val=$(( 2 + 2 ))
echo "两数之和为 : $val"

```

**两点注意**

* 表达式和运算符之间要有空格
* 完整的表达式要被 ` ` 包含

### 算术运算符

|运算符   说明
|---  |---   |
|`+ ` |加法  |
|`- ` |减法  |
|`* ` |乘法  |
|`/ ` |除法  |
|`% ` |取余  |
|`= ` |赋值  |
|`==` |相等  |
|`!=` |不相等|

**注意**

* 条件表达式要放在方括号之间，并且要有空格，例如: [$a==$b] 是错误的，必须写成 [ $a == $b ]
* 乘号`*`前边必须加反斜杠`\`才能实现乘法运算

### 关系运算符

关系运算符只支持数字，不支持字符串，除非字符串的值是数字

|运算符|   说明|
|---   |---    |
|-eq   |检测两个数是否相等，相等返回 true|
|-ne   |检测两个数是否相等，不相等返回 true|
|-gt   |检测左边的数是否大于右边的，如果是，则返回 true|
|-lt   |检测左边的数是否小于右边的，如果是，则返回 true|
|-ge   |检测左边的数是否大于等于右边的，如果是，则返回 true|
|-le   |检测左边的数是否小于等于右边的，如果是，则返回 true|

### 布尔运算符

|运算符| 说明|
|---   |---  |
|!     | 非运算，表达式为 true 则返回 false，否则返回 true|
|-o    | 或运算，有一个表达式为 true 则返回 true|
|-a    | 与运算，两个表达式都为 true 才返回 true|

### 逻辑运算符

|运算符  说明
|---  |---  |
|`&&` |逻辑的 AND|
|`||` |逻辑的 OR |

**注意**

* 逻辑运算表达式要放在[[  ]]里面
* [[  ]] 是 [ ] 的扩充，能够支持<,>符号运算不需要转义符，它还是以字符串比较大小

### 字符串运算符

|运算符 |说明 |
|---    |---  |
|=   | 检测两个字符串是否相等，相等返回 true|
|!=  | 检测两个字符串是否相等，不相等返回 true|
|-z  | 检测字符串长度是否为0，为0返回 true|
|-n  | 检测字符串长度是否为0，不为0返回 true|
|str | 检测字符串是否为空，不为空返回 true|

### 文件测试运算符

文件测试运算符用于检测 Unix 文件的各种属性

|操作符| 说明|
|---   |---  |
|-b file  |检测文件是否是块设备文件，如果是，则返回 true|
|-c file  |检测文件是否是字符设备文件，如果是，则返回 true|
|-d file  |检测文件是否是目录，如果是，则返回 true|
|-f file  |检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true|
|-g file  |检测文件是否设置了 SGID 位，如果是，则返回 true|
|-k file  |检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true|
|-p file  |检测文件是否是有名管道，如果是，则返回 true|
|-u file  |检测文件是否设置了 SUID 位，如果是，则返回 true|
|-r file  |检测文件是否可读，如果是，则返回 true|
|-w file  |检测文件是否可写，如果是，则返回 true|
|-x file  |检测文件是否可执行，如果是，则返回 true|
|-s file  |检测文件是否为空（文件大小是否大于0），不为空返回 true|
|-e file  |检测文件（包括目录）是否存在，如果是，则返回 true|

---


## Shell 流程控制

**流程控制不可为空**

### if else

**if 语句语法格式**

```
if condition; then
    command1
    command2
    ...
    commandN
fi
```

写成一行

```
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi
```

**if else 语法格式**

```
if condition; then
    command1
    command2
    ...
    commandN
else
    command
fi
```

**if else-if else 语法格式**

```
if condition1; then
    command1
elif condition2; then
    command2
else
    commandN
fi
```

###for 循环

**for循环一般格式为**

```
for var in item1 item2 ... itemN; do
    command1
    command2
    ...
    commandN
done
```

**写成一行**

```
for var in item1 item2 ... itemN; do command1; command2… done;
```

当变量值在列表里，for循环即执行一次所有命令，使用变量名获取列表中的当前取值。命令可为任何有效的shell命令和语句。in列表可以包含替换、字符串和文件名。

in列表是可选的，如果不用它，for循环使用命令行的位置参数。

**顺序输出当前列表中的数字**

```
for loop in 1 2 3 4 5; do
    echo "The value is: $loop"
done
```

**顺序输出字符串中的字符**

```
for str in 'This is a string'; do
    echo $str
done
```

###while 语句

while循环用于不断执行一系列命令，也用于从输入文件中读取数据；命令通常为测试条件

```
while condition; do
    command
done
```

**while循环可用于读取键盘信息**

```
while read FILM; do
    echo "是的！$FILM 是一部好电影"
done
```

###无限循环

**无限循环语法格式**

```
while :; do
    command
done
```

或者

```
while true; do
    command
done
```

或者

```
for (( ; ; ))
```

###until 循环

until循环执行一系列命令直至条件为真时停止。

**until 语法格式**

```
until condition; do
    command
done
```

###case

Shell case语句为多选择语句。可以用case语句匹配一个值与一个模式，如果匹配成功，执行相匹配的命令

```
case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2）
    command1
    command2
    ...
    commandN
    ;;
esac
```

case工作方式如上所示。取值后面必须为单词in，每一模式必须以右括号结束。取值可以为变量或常数。匹配发现取值符合某一模式后，其间所有命令开始执行直至 ;;。

取值将检测匹配的每一个模式。一旦模式匹配，则执行完匹配模式相应命令后不再继续其他模式。如果无一匹配模式，使用星号 * 捕获该值，再执行后面的命令。

###跳出循环

在循环过程中，有时候需要在未达到循环结束条件时强制跳出循环，Shell使用两个命令来实现该功能：break和continue。

**break**

break命令允许跳出所有循环（终止执行后面的所有循环）。

**continue**

continue命令与break命令类似，只有一点差别，它不会跳出所有循环，仅仅跳出当前循环。

**esac**

它需要一个esac（就是case反过来）作为结束标记，每个case分支用右圆括号，用两个分号表示break。

---

##Shell 函数


###shell中函数的定义格式如下

[ function ] funname () {
    action;

    [return int;]
}

**说明**

1. 可以带function fun() 定义，也可以直接fun() 定义,不带任何参数
2. 数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255)
3. 函数返回值在调用该函数后通过 $? 来获得
4. 所有函数在使用前必须定义,调用函数仅使用其函数名即可

### 函数参数

|参数处理 |说明|
|--- |--- |
|`$n`|  第n个参数|
|`$#`|  传递到脚本的参数个数|
|`$*`|  以一个单字符串显示所有向脚本传递的参数|
|`$$`|  脚本运行的当前进程ID号|
|`$!`|  后台运行的最后一个进程的ID号|
|`$@`|  与`$*`相同，但是使用时加引号，并在引号中返回每个参数。|
|`$-`|  显示Shell使用的当前选项，与set命令功能相同。|
|`$?`|  显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。|

---

## 调试参数

在 Bash 脚本中，使用 set -x 去调试输出（或者使用它的变体 set -v，它会记录原始输入，包括多余的参数和注释）。
set -e 令脚本在发生错误时退出而不是继续运行；
set -u 来检查是否使用了未赋值的变量；
set -o pipefail，它可以监测管道中的错误。
当牵扯到很多脚本时，使用 trap 来检测 ERR 和 EXIT。
一个好的习惯是在脚本文件开头这样写，这会使它能够检测一些错误，并在错误发生时中断程序并输出信息：

```
set -euo pipefail
trap "echo 'error: Script failed: see failed command above'" ERR
```
