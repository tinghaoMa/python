#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    返回函数
    高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
    返回闭包时牢记一点：
        返回函数不要引用任何循环变量，或者后续会发生变化的变量。

    https://www.cnblogs.com/z360519549/p/5172020.html
    python引用变量的顺序： 当前作用域局部变量->外层作用域变量->当前模块中的全局变量->python内置变量 。
"""

# 不返回求和的结果，而是返回求和的函数


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f1 = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
# 调用函数f时，才真正计算求和的结果
print(f1())
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
print(f1)
print(f2)
print(f1 == f2)


# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 全部都是等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f3, f4, f5 = count()

print(f3())
print(f4())
print(f5())


# 循环变量怎么办？ 1 4 9
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：


def count2():
    def f(j):
        def f():
            return j * j
        return f
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count2()
print(f1())
print(f2())
print(f3())


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

# def createCounter():
#     a = 0
#
#     def counter():
#         nonlocal a
#         a += 1
#         return a
#     return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
