#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    字符串
"""
"""
    %d	整数
    %f	浮点数
    %s	字符串 会把任何数据类型转换为字符串
    %x	十六进制整数
"""
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# 字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：

print('growth rate: %d %%' % 7)

# format
print('Hello, {0}, 成绩提升了 {1:.1f}%  {2}'.format('小明', 17.125, '呵呵'))
