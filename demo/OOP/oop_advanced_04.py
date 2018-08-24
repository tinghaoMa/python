#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    定制类
    __slots__    __len__
    Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

    __str__() __repr__()

    __iter__ __next__ __getitem__

    __call__ 实力本身上面调用方法
'''
import time

# __str__()返回用户看到的字符串
# __repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student name=%s' % self.name
#
#     __repr__ = __str__
#
#
# print(Student('ls'))
# stu = Student('zs')
# print(stu)

class Count(object):
    def __init__(self, num=0):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        self.num = self.num + 1
        return self.num

    def __getitem__(self, n):
        for x in range(0, n):
            self.num = self.num + 1
        return self.num

    # __getattr__默认返回就是None
    def __getattr__(self, attr):
        if attr == 'score':
            return 190
        else:
            return '没有这个属性'

# print(dir(time))

# 如果想要遍历 需要实现__iter__和__next__这2个方法
# for x in Count():
#     time.sleep(3)
#     print(x)


# 按照下标取出元素 需要复写 __getitem__
print(Count()[3])
print(Count()[13])

print(Count().score)
print(Count().age)


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain('www.baidu.com').status.user.timeline.list)


# __call__
class Person(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('Person name = %s' % self.name)


# 对象看成函数，把函数看成对象
p = Person('smallegg')
p()
print(max(1, 2))

# 判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print(callable(p))
print(callable(max))
print(callable([1, 2, 3]))
print(callable((1, 2, 3)))
print(callable('abc'))
