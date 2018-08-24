#!/user/bin/python3
#  -*- coding: utf-8 -*-
"""
    IO
        1.open() 打开文件如果文件不存在抛出IOError错误
        2.read() 一次读取文件的所有内容,用一个str表示
        3.close() 读取文件之后必须关闭 否则会占用先关系统资源
"""
# try:
#     f = open('demo/resources/hello.py', 'r')
#     print(f.read())
# except Exception as e:
#     print('except: ', e)
# finally:
#     if f:
#         f.close()

# 简便操作
# with open('demo/IO/hello.py', 'r') as f:
#     print(f.read())


# 读取大文件
# path = 'demo/resources/GankAndroidAdapter.java'
# with open(path, 'r') as f:
#     for line in f.readlines():
#         print(line.strip())

# 读取二进制文件(图片 视频)
# file_img = open('demo/resources/9-1FPGH525.jpg', 'rb')
# print(file_img.read())
# file_img.close()

# 读取指定类型的文件 对于一些非法字符可以使用errors='ignore' 忽略
gbkPath = 'demo/resources/hello.txt'
with open(gbkPath, 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())
