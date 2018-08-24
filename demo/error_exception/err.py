#!/user/bin/python3
#  -*- coding: utf-8 -*-
'''
    python3 -m pdb demo / error_exception / err.py
    启动调试模式
        1.l 查看源代码
        2.n 单步执行
        3.任何时候都可以输入命令p 变量名来查看变量
        4.输入命令q结束调试
        5.命令c继续运行
'''
import pdb

s = '0'
n = int(s)
pdb.set_trace()  # pdb.set_trace()，就可以设置一个断点 运行到这里自动暂停
print(10 / n)
