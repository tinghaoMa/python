#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    Python内建的filter()函数用于过滤序列。
    filter()也接收一个函数和一个序列。和map()不同的是，
    filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
"""

# 只显示队列中的基数


def is_odd(x):
    return x % 2 == 1


L = list(range(20))
print(list(filter(is_odd, L)))

# 把一个序列中的空字符去掉


def not_empty(x):
    return x and x.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
