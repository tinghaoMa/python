#!/user/bin/python3
#  -*- coding: utf-8 -*-
'''
    继承和多态
    继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
    子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
    动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的
'''


class Animal(object):
    def run(self):
        print('Animal can run')


class Dog(Animal):
    def run(self):
        print('Dog can run')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    pass


def run_twice(animal):
    animal.run()
    animal.run()


dog = Dog()
run_twice(dog)

cat = Cat()
run_twice(cat)

# 动态语言 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以


class Timer(object):
    def run(self):
        print('Start...')


t = Timer()
run_twice(t)
