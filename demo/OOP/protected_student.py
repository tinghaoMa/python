#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    私有变量 使用2个下划线 __开头定义
    在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
    特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
'''


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 不能直接访问__所以，仍然可以通过_Student__name来访问__name变量
print('DO NOT use bart._Student__name:', bart._Student__name)
