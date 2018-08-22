#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    高级特性
        切片
        迭代 使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行
        列表生成式
"""
import os
from collections import Iterable

# 切片
L = ['a', 'b', 'c', 'd', 'e']
# 从索引0开始取，直到索引3为止，但不包括索引3
print(L[0:3])

# 如果是0开始可以省略
print(L[:3])

# 倒叙取 记住倒数第一个元素的索引是-1。
print(L[-2:])
print(L[-3:-1])


L = list(range(100))
# 前10个数，每两个取一个：
print(L[:10:2])

# 所有数，每5个取一个：
print(L[::5])

# 什么都不写，只写[:]就可以原样复制一个list：
L2 = L[:]
L2[0] = 100
print(L2)


'''
    tuple也可以用切片操作
'''
print((1, 2, 3, 4, 5, 6)[:3])


# 字符串

print('ABCDEF'[1:3])
print('ABCDEFG'[::2])

# 去除首尾空格


def trim(s):
    while len(s) > 0 and s[0] == ' ':
        s = s[1:]
    while len(s) > 0 and s[-1] == ' ':
        s = s[:-1]
    return s


s = '   hello world   '
print(trim(s))
print(s)

# 迭代
print('\n迭代')
d = {'a': 1, 'b': 2, 'c': 3}
# 迭代key
for key in d:
    print('key =%s' % key)
# 迭代value
for value in d.values():
    print('value =%s' % value)
# 同事迭代key 和value
for k, v in d.items():
    print('key =%s' % k, 'value =%s' % v)

# 迭代字符串
for ch in 'ABCDED':
    print('ch =%s' % ch)

# 判断是否是可以迭代的对象
print(isinstance('ABC', Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance({'city': 'beijing', 'age': 20}, Iterable))
print(isinstance(123, Iterable))  # 整数不可以迭代


# 获取元素下标
for index, value in enumerate(['a', 'v', 'c']):
    print('index =%d' % index, 'value =%s' % value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


# 列表生成式
print(list(range(1, 11)))

L = [x * x for x in range(1, 11)]
print(L)

# 删选偶数的平方
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

# 两层循环，可以生成全排列
L = [m + n for m in 'ABC' for n in '123']
print(L)

# for x in '123':
#     print(isinstance(x, int))
#     print(isinstance(x, str))

files = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
print(files)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print('k = %s' % k, 'v = %s' % v)

L = [k + '=' + v for k, v in d.items()]
print(L)

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


L = ['Hello', 'World', 18, 'Apple', None]

print([s.lower() for s in L if isinstance(s, str)])
