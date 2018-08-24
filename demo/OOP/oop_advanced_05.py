#!/user/bin/python3
#  -*- coding: utf-8 -*-
"""
    枚举
"""
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# print(dir(Month))
# print(Month.__class__)
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


"""
    Enum派生出自定义类
"""


@unique
class Weekend(Enum):
    NONE = 0
    WIFI = 1
    G3 = 2
    G4 = 3

#
# for name, member in Weekend.__members__.items():
#     print(name, '=>', member, ',', member.value)


print(Weekend(1))
print(Weekend.WIFI)
