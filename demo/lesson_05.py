#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    dict
        Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，
        使用键-值（key-value）存储，具有极快的查找速度
        dict有以下几个特点：
            1.查找和插入的速度极快，不会随着key的增加而变慢；
            2.需要占用大量的内存，内存浪费多。
            3.dict是用空间来换取时间的一种方法。
    set
        set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
"""

Dict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(Dict['Michael'])

# 通过in判断key是否存在
print('Bob' in Dict)
print('Mth' in Dict)

# dict提供的get()方法，如果key不存在，可以返回None
print(Dict.get('Thomas'))
# 指定返回值
print(Dict.get('Thomas', 'hello'))

# 删除一个key
print(Dict.pop('Bob'))
print(Dict)

# set

s = set([1, 2, 3, 1])
print(s)

# 添加一个元素
s.add(4)
print(s)

# 删除一个元素
s.remove(4)
print(s)

s.add('hello')
print(s)
