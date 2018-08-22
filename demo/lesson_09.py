#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    生成器 generator
    可以按照某种算法推算出后续元素,因为此不必创建完整的list,避免占用大量内存空间
"""
# 第一种方法很简单，只要把一个列表生成式的[]改成()
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)
# 通过for循环来迭代它
for x in g:
    print(x)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(6)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for x in fib(6):
    print(x)


def test(lineNum):
    L = [1]  # 初始值
    n = 0
    while n <= lineNum:
        yield(L)
        maxIndex = len(L) - 1  # 最大下标，下标从0开始
        # range(0,n)时，取的是0~(n-1)范围的数
        # 第二次获取时,len=1,range(0)=[],因此k=[],L=[1,1]
        # 第三次获取时,len=2,range(0,1)=[0],k=[2],L=[1,2,1]
        # 第四次获取时,len=3,range(0,2)=[0,1],k=[L[0]+L[1],L[1]+L[2]]]=[3,3],L=[1,3,3,1]
        k = [L[j] + L[j + 1] for j in range(maxIndex)]
        L = [1] + k + [1]
        n = n + 1


for x in test(10):
    print(x)
