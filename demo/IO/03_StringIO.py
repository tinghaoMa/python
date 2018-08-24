#!/user/bin/python3
#  -*- coding: utf-8 -*-
"""
    StringIO 只能操作str
    数据读写不一定是文件，也可以在内存中读写。
    StringIO顾名思义就是在内存中读写str
"""
from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!\n')
print(f.getvalue())

f1 = StringIO('hello!\nworld!\n')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s)
