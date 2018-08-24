#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Python内置的@property装饰器就是负责把一个方法变成属性调用的

    只读属性，只定义getter方法，不定义setter方法就是一个只读属性
'''


# class Student(object):
#
#     def get_score(self):
#         return self.score
#
#     def set_score(self, score):
#         if not isinstance(score, int):
#             raise ValueError('score must Integer')
#         if(score not in(0, 100)):
#             raise ValueError('score must between 0 ~ 100!')
#         else:
#             self.score = score
#
#
# stu = Student()
# stu.set_score(100)
# print(stu.get_score())


class Student(object):
    # 把一个getter方法变成属性，只需要加上@property就可以了
    @property
    def score(self):
        return self._score

    # 负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 只读属性
    @property
    def age(self):
        return 18


stu = Student()
stu.score = 100
print(stu.score)
# stu.score = 1000

# stu.age = 30
print('只读属性', stu.age)
