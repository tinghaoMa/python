#!/user/bin/python3
#  -*- coding: utf-8 -*-
"""

"""
import os
import shutil

# print(dir(os))
# print(os.name)
# print(os.uname())
# print(os.environ)
# print(os.environ.get('PATH'))
# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
testDirPath = os.path.join(os.path.abspath('.') + '/demo/resources', 'testDir')
# 创建一个目录
# os.mkdir(testDirPath)
# 删掉一个目录 只能删除空目录:
# os.rmdir(testDirPath)

# shutil.rmtree 只要是目录都可以删除不管有没有内容
# notEmptyDir = os.path.join(os.path.abspath(
#     '.') + '/demo/resources', 'removeDir')
# shutil.rmtree(notEmptyDir)

# 拆分路径
print(os.path.split('/Users/itck_mth/study/python/a.txt'))
print(os.path.split('/Users/itck_mth/study'))
# 直接得到文件后缀
print(os.path.splitext('/Users/itck_mth/study/python/a.txt'))

# 文件创建
f = open('demo/resources/1.txt', 'w')
f.close()
# 文件重命名
os.rename('demo/resources/1.txt', 'demo/resources/newName.txt')

# 删除文件
# os.remove('demo/resources/newName.txt')


# 文件的拷贝
shutil.copyfile('demo/resources/newName.txt', 'demo/resources/newNameCopy.txt')

# 移动文件
shutil.move('demo/resources/newNameCopy.txt', 'demo/resources/destDir')
