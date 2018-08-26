#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    多进程
    multiprocessing模块就是跨平台版本的多进程模块
"""

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()  # 调用一次返回两次 子进程永远返回0
if pid == 0:
    print('I am 子进程 (%s) and my parent is %s.' %
          (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
