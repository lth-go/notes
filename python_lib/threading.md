# NAME
**threading**

## CLASSES:

class **Thread**(Verbose):

*方法:

def **__init__**(
        group=None,
        target=None,
        name=None,
        args=(),
        kwargs={}
    )
>   group是预留的，用于将来扩展；
>   target是一个可调用对象,在线程启动后执行；
>   name是线程的名字。默认值为“Thread-N“，N是一个数字。
>   args和kwargs分别表示调用target时的参数列表和关键字参数。

def **is_alive**()
>   判断线程是否是激活的（alive）。从调用start()方法启动线程，到run()方法执行完毕或遇到未处理异常而中断 这段时间内，线程是激活的。

def **join**([timeout])
>   调用Thread.join将会使主调线程堵塞，直到被调用线程运行结束或超时。参数timeout是一个数值类型，表示超时时间，如果未提供该参数，那么主调线程将一直堵塞到被调线程结束。下面举个例子说明join()的使用：

def **run**()
>   重写函数来支持类继承式多线程

def **setDaemon**(daemonic)
>   设置守护进程

def **start**()
>   运行线程

*属性:

**daemon**
>   是否为守护线程

**ident**
>   获取线程的标识符。线程标识符是一个非零整数，只有在调用了start()方法之后该属性才有效，否则它只返回None。

**name**
>   用于获取和设置线程的名称

---

class **Lock**
Lock.acquire()
获得锁
Lock.release()
释放锁


threading.RLock:
RLock允许在同一线程中被多次acquire

RLock.acquire()
获得锁
RLock.release()
释放锁


threading.Condition:

Condition.acquire()
获得锁
Condition.release()
释放锁

Condition.wait([timeout]):
wait方法释放内部所占用的琐，同时线程被挂起，直至接收到通知被唤醒或超时（如果提供了timeout参数的话）。当线程被唤醒并重新占有琐的时候，程序才会继续执行下去。

Condition.notify():
唤醒一个挂起的线程（如果存在挂起的线程）。注意：notify()方法不会释放所占用的琐。

Condition.notify_all()
唤醒所有挂起的线程（如果存在挂起的线程）


threading.Event:
Event.wait([timeout])

堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）。
Event.set()

将标识位设为Ture
Event.clear()

将标识伴设为False。
Event.isSet()

判断标识位是否为Ture。

threading.Timer:
指定一定时间间隔后执行一个函数

threading.local:
存储特定线程的值

hreading.active_count()

获取当前活动的(alive)线程的个数。
threading.current_thread()

获取当前的线程对象（Thread object）。
threading.enumerate()

获取当前所有活动线程的列表。
threading.settrace(func)

设置一个跟踪函数，用于在run()执行之前被调用。
threading.setprofile(func)

设置一个跟踪函数，用于在run()执行完毕之后调用。
