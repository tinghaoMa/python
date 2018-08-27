#!/user/bin/python3
#  -*- coding: utf-8 -*-
'''
    collections
    namedtuple可以很方便地定义一种数据类型,
    创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
'''
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

'''
    deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
'''
q = deque(['1', '2', '3', '4'])
q.append('x')
q.appendleft('y')
q.pop()
q.popleft()
print(q)

'''
    defaultdict
    使用dict时，如果引用的Key不存在，就会抛出KeyError。
    如果希望key不存在时，返回一个默认值，就可以用defaultdict：
'''
dd = defaultdict(lambda: 'N/A')

dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])


'''
    OrderedDict
    使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
    如果要保持Key的顺序
    python3.6以后dict都是有序的
'''
d = dict([('a', 1), ('e', 2), ('c', 3), ('d', 3), ('b', 3)])
for k, v in d.items():
    print(k, v)

od = OrderedDict([('a', 1), ('e', 2), ('c', 3), ('d', 3), ('b', 3)])
print(od)
for k, v in od.items():
    print(k, v)


'''
    Counter 计数器
'''
# 统计字符出现的次数
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
