#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    高阶函数
    sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
"""
print(sorted([36, 5, -12, 9, -21]))

# key函数来实现自定义的排序按绝对值大小
L = sorted([36, 5, -12, 9, -21], key=abs)
print(L)
