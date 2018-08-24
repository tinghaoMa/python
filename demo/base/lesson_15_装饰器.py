#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    装饰器 Decorator
    在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
    OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，
    直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
    decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
"""
import functools

# 装饰器 不想改变now功能 但是希望增加相关日志
# 改完函数的名字会变
#
# def log(func):-
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# def log2(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('call %s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def now():
    print('2018-08-23 16:34:43')


@log2('hello world')
def now2():
    print('2018年08月23日16:50:16')


# f = now
# print(f.__name__)
# now()
# print(now.__name__)
# print('\n')
# now2()
# print(now2.__name__)


#  begin call   end call

def logTest(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call %s():' % func.__name__)
        result = func(*args, **kw)
        print('end call %s():' % func.__name__)
        return result
    return wrapper


@logTest
def test():
    print('hello world')
    return '123456'


print(test())
