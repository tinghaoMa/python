#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

'''
from types import MethodType


class Student(object):
    pass


s = Student()
print(s)
# 给动态实例绑定一个属性
s.name = 'zs'
print(s.name)

# 给实例绑定一个方法 给一个实例绑定的方法，对另一个实例是不起作用


def set_age(self, age):
    self.age = age


print(hasattr(s, 'set_age'))
s.set_age = MethodType(set_age, s)
print(hasattr(s, 'set_age'))
s.set_age(100)
print(s.age)

# 给所有实例都绑定方法，可以给class绑定方法,class绑定方法后，所有实例均可调用：


def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(30)
print(s.score)


'''
    限制实例的属性 使用__slots__
    __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用
'''


class Person(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


p = Person()
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
# p.score = 100


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 40
print(g.score)
