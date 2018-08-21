#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    函数
        定义函数时，需要确定函数名和参数个数；
        如果有必要，可以先对参数的数据类型做检查；
        函数体内部可以用return随时返回函数结果；
        函数执行完毕也没有return语句时，自动return None。
        函数可以同时返回多个值，但其实就是一个tuple。

"""
import math

# 内置函数
print(abs(-10))
print(max(1, 22))

# 数据类型转换
print('int(\'123\') =%d' % int('123'))
print(' str(1.23) = %s' % str(1.23))
print(' bool(1) ', bool(1))
print(' bool(0) ', bool(0))

# 函数名其实就是指向一个函数对象的引用
a = abs
print(a(-100))

# 定义函数
# 绝对值函数 参数类型做检查


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if (x > 0):
        return x
    else:
        return -x


print(my_abs(10))
print(my_abs(-10))

# my_abs('A')

# 函数返回多个值 返回多值其实就是返回一个tuple


def test(a, b):
    a1 = a * 3 + 100
    b1 = b * 3
    return a1, b1


x, y = test(10, 20)
print('x = %d' % x, 'y = %d' % y)

print(test(10, 20))

# 空函数  实际上pass可以用来作为占位符


def nop():
    pass


print(math.sqrt(2))
