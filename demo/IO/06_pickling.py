#!/user/bin/python3
#  -*- coding: utf-8 -*-
'''
    变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
    Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
    并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，
    不能成功地反序列化也没关系。

    Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
'''
import json
import os
import pickle

d = {'name': 'Bob', 'age': 20, 'score': 88}
d1 = dict(name='Bob', age=20, score=88)

destPath = os.path.join('demo/resources', 'pickling.txt')
print(destPath)
# 直接序列化
f = open(destPath, 'wb')
pickle.dump(d, f)
f.close()


# 反序列化
f = open(destPath, 'rb')
d = pickle.load(f)
f.close()
print('pickle 反序列化 ', d)

# json序列化
destJsonPath = os.path.join('demo/resources', 'json.txt')
f = open(destJsonPath, 'w')
json.dump(d, f)
f.close()
# json反序列化
f = open(destJsonPath, 'r')
d = json.load(f)
f.close()
print('json 反序列化 ', d)
