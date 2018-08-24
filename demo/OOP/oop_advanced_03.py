#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    多重继承
    MixIn的目的就是给一个类增加多个功能，
    这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，
    而不是设计多层次的复杂的继承关系。
    只要选择组合不同的类的功能，就可以快速构造出所需的子类
'''


class Animal(object):
    pass

# 大类:


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')

# 各种动物:


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Runnable):
    pass


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird, Flyable):
    pass
