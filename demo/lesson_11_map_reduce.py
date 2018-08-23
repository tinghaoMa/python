#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    高阶函数
    Python内建了map()和reduce()函数。
"""
from functools import reduce

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


print(list(map(double, L)))

# list所有数字转为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7])))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(list(map(char2num, '135789')))

'''
    reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
    reduce把结果继续和序列的下一个元素做累积计算
'''


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))

# 练习 首字母变成大写 其他的字母小写
L = ['adam', 'LISA', 'barT']


def normalize(name):
    return name[0].upper() + name[1:].lower()


print(list(map(normalize, L)))

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：


def prod(L):
    def count(x, y):
        return x * y
    return reduce(count, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

s = '111.22'
s1 = s.split('.', 1)


def sz(s):
    dig = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
           '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return dig[s]


def cc1(x, y):
    return x * 10 + y


# 111+22*0.01
h = reduce(cc1, map(sz, s1[0])) + reduce(cc1,
                                         map(sz, s1[1])) * pow(10, -(len(s1[1])))
print(h)
