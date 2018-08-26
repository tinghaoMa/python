#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    线程池
    启动大量的子进程，可以用进程池的方式批量创建子进程
"""
import os
import random
import time
from multiprocessing import Pool


def log_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent Process id  %s' % os.getpid())
    p = Pool(4)  # 同时跑4个进程
    for x in range(4):
        p.apply_async(log_time_task, args=(x,))
    print('wait for all subprocess done')
    p.close()
    p.join()
    print('all  subprocess done')
