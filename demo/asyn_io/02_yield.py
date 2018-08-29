#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# def h():
#     print ('Wen Chuan')
#     yield 5
#     print ('Fighting!')
#
#
# c = h()
# print(c)
# c.__next__()
# c.__next__()

def h():
    r = 'asdasd'
    print ('Wen Chuan')
    m = yield r  # Fighting!
    print ('m = %s' % m)
    r = 'hello world'
    d = yield 12
    print('d = %s' % d)
    print ('We are together!')
    yield 3


# c = h()
# print('开始')
# r = c.send(None)
# print('r = %s' % r)
# print('第二次')
# r = c.send('Fighting!')  # (yield 5)表达式被赋予了'Fighting!'
# print('111-----r = %s' % r)
# print('第三次')
# r = c.send('Fighting!111111')  # (yield 5)表达式被赋予了'Fighting!'
# print('22222-----r = %s' % r)


def gen_example():
    print ('before any yield')

    yield 'first yield'

    print ('between yields')

    yield 'second yield'

    print ('no yield anymore')


gen = gen_example()
print(gen.__next__())
print(gen.__next__())
