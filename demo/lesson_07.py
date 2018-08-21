#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    函数的参数
"""
# 位置参数 函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 2))
print(power(5, 3))


# 默认参数
'''
    设置默认参数时，有几点要注意
        一是必选参数在前，默认参数在后
        二是如何设置默认参数。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
    使用默认参数有什么好处？
        最大的好处是能降低调用函数的难度。

    定义默认参数要牢记一点：默认参数必须指向不变对象！
'''


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(5, 3))

# 默认参数有个最大的坑


def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end())

# 如何避免


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end())


# 可变参数
'''
    可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
'''


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
print(calc(1, 2, 3, 5))


nums = (1, 2, 3)
print(calc(nums[0], nums[1], nums[2]))
print(calc(*nums))


# 关键字参数
'''
    允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
'''


def person(name, age, **kw):
    print('person name :', name, ' age =', age, 'other = ', kw)


def person2(name, age, **kw):
    kw['city'] = '上海'
    print('person2 name :', name, ' age =', age, 'other = ', kw)


person('zs', 20, city='Beijing', job='Doctor')
# 简化写法
extra = {'city': 'Beijing', 'job': 'Engineer'}
'''
    **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
    kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
'''
person2('ls', 30, **extra)

print('原来的值不变', extra)


# 命名关键字参数
'''
    限制关键字参数的名字，就可以用命名关键字参数
    关键字参数和命名关键字参数的区别在于，前者可以传递任何名字的参数，而后者只能传递*后面名字的参数。
'''


def person(name, age, *, city, job):
    print(name, age, city, job)


person('zs', 122, city='Beijing', job='Engineer')

'''
    如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
'''


def person(name, age, *args, city, job):
    print(name, age, city, job)


person('zs', 122, city='Beijing', job='Engineer')

# 默认参数


def person(name, age, *args, city='DaLian', job):
    print(name, age, city, job)


person('zs', 122, job='Engineer')
