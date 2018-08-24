#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    list and tuple
    list是一种有序的集合，可以随时添加和删除其中的元素 list里面的元素的数据类型也可以不同
    tuple 有序列表叫元组 tuple一旦初始化就不能修改 没有append()，insert()这样的方法
"""
classmates = ['a', 'b', 'c']
print(classmates)
print('classmates的大小是 %d' % len(classmates))
# 正序读取
print(classmates[0])
print(classmates[1])
print(classmates[2])
# 倒叙读取
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

# 追加元素 到末尾
classmates.append('d')
print(classmates)

# 在指定位置插入元素
classmates.insert(0, 'first')
print(classmates)

# 删除list末尾
classmates.pop()
print(classmates)

# 删除指定位置的元素
print(classmates.pop(1))
print(classmates)

# 把某个元素替换成别的元素
classmates[1] = 'hello world'
print(classmates)


# 元素类型不同
L = ['Apple', 123, True]
print(L)

# 空
M = []
print('空的list %d' % len(M))


# tuple
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print (t)
t = ()
print (t)
"""
    定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，
    这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
    所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
"""
t = (1,)
print (t)


"""
    “可变的”tuple
    其实变的不是tuple的元素，而是list的元素。
    tuple一开始指向的list并没有改成别的list，
    所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
"""
t = (1, 2, [3, 4])
print(t)
print(t[2])
t[2][0] = 'hello'
t[2][1] = 'python'
print(t)
