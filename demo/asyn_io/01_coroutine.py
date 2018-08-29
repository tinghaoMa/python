#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    协程的特点是一个线程执行
    优势:
    1.协程极高的执行效率
      因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销
    2.不需要多线程的锁机制
     因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，
     只需要判断状态就好了，所以执行效率比多线程高很多。

    协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程

    某个函数包含了yield，这意味着这个函数已经是一个Generator
'''
#
#
# def h():
#     print ('To be brave')
#     yield 5
#     print ('1111111')
#
#
# c = h()
# c.__next__()


def consume():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] Consuming %s....' % n)
        r = '200 ok'


def produce(c):
    c.send(None)  # 启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[Producer] Producing %s....' % n)
        r = c.send(n)
        print('[Producer] Consumer return %s...' % r)
    c.close()


c = consume()
produce(c)
