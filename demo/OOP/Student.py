#!/user/bin/python3
#  -*- coding: utf-8 -*-
"""
    面向对象
"""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))


stu1 = Student('zs', 20)
# Python允许对实例变量绑定任何数据
stu1.age = 100
stu1.print_score()
print(stu1.age)


stu2 = Student('ls', 40)
stu2.print_score()

print(stu1)
print(Student)
