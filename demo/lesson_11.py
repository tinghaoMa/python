#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    高阶函数
    Python内建了map()和reduce()函数。
"""
# 函数本身也可以赋值给变量，即：变量可以指向函数
f = abs
print(f(-10))

# 传入函数


def add(x, y, f):
    return f(x) + f(y)


print(add(10, -20, abs))

'''
    map()函数接收两个参数，一个是函数，一个是Iterable，
    map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''
L = list(range(10))
print(L)


def double(x):
    return x * x


value = map(double, L)
print(list(value))
