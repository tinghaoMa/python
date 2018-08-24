#!/user/bin/python
#  -*- coding: utf-8 -*-
"""
    条件判断
        if <条件判断1>:
            <执行1>
        elif <条件判断2>:
            <执行2>
        elif <条件判断3>:
            <执行3>
        else:
            <执行4>
"""
# 注意不要少了冒号
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 简写
if 1:
    print('True')

'''
    循环
    第一种 :for...in
    第二种 :while
'''
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# range()函数，可以生成一个整数序列 list()函数可以转换为list

L = list(range(5))

print(L)


L = ['Bart', 'Lisa', 'Adam']
n = 0
while n < len(L):
    print (L[n])
    n += 1

# break
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
