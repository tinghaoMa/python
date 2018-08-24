#!/user/bin/python3
#  -*- coding: utf-8 -*-
"""
    对象属性 和类属性
    如果名字相同 对象属性优先级大于 类属性
"""


class Student(object):
    name = 'hello world'

    def __init__(self, name):
        self.name = name


s = Student('zs')
print(s.name)
print(Student.name)

# 删除实例的属性 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
del s.name
print(s.name)
