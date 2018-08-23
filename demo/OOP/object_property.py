#!/user/bin/python3
#  -*- coding: utf-8 -*-
"""
    对象属性 类型判断
"""
import types


def test():
    pass


print(type(123))
print(type('abc'))
print(type(test))
print(type(abs))

print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(test, types.FunctionType))

'''
 获得一个对象的属性和方法
 如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
'''
print(dir('abc'))

print(len('abc'))
print('abc'.__len__())


class MyObject(object):
    def __init__(self, name):
        self.name = name

    def power(self):
        return 10


obj = MyObject('zs')

print(hasattr(obj, 'name'))
print(getattr(obj, 'name'))
setattr(obj, 'name', 'ls')
print(getattr(obj, 'name'))
# 可以传入一个default参数，如果属性不存在，就返回默认值

print(getattr(obj, 'age', 20))


print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())
