#!/user/bin/python3
#  -*- coding: utf-8 -*-
"""
    BytesIO
    实现了在内存中读写bytes
"""
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())
