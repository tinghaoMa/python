#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    匿名函数
"""
'''
    lambda x: x * x 就是匿名函数
    def f(x): return x * x
'''
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6])))

'''
    匿名函数可以赋值给变量
    f = lambda x: x * x
    f(5)
'''

# 匿名函数作为返回值返回


def build(x, y):
    return lambda: x * x + y * y


print(build(1, 2)())

# is_odd 改变成匿名函数


def is_odd(n):
    return n % 2 == 1


L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
