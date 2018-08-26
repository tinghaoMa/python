#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    多线程
    Python的标准库提供了两个模块：_thread和threading，
    _thread是低级模块，threading是高级模块，对_thread进行了封装。
    绝大多数情况下，我们只需要使用threading这个高级模块



    任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
    Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
    主线程实例的名字叫MainThread，
    子线程的名字在创建时指定，我们用LoopThread命名子线程

"""
import threading
import time

# 新线程执行的代码:


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
