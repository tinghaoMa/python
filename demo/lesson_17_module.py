#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'  # 作者

import sys


def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


'''
    通过_前缀来实现一个私有方法或者私有变量 外部不应该引用
    类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
'''


def _count():
    print('我是一个私有方法 别的模块引用不到')


if __name__ == '__main__':
    test()
