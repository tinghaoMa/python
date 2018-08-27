#!/user/bin/python3
#  -*- coding: utf-8 -*-
'''
    datetime是Python处理日期和时间的标准库。
    注意到datetime是模块，datetime模块还包含一个datetime类，
    通过from datetime import datetime导入的才是datetime这个类。
    如果仅导入import datetime，则必须引用全名datetime.datetime。
    datetime.now()返回当前日期和时间，其类型是datetime。
'''
# import datetime
#
# now = datetime.datetime.now()
# print(now)
# print(type(now))


from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(type(now))

# 用指定日期时间创建datetime
dt = datetime(2018, 8, 27, 13, 48)
print(dt)

# 把datetime转换为timestamp
print(dt.timestamp())

# timestamp转换为datetime
t = 1535348880.0
print(datetime.fromtimestamp(t))

# str转换为datetime
cday = datetime.strptime('2018-8-27 13:53:41', '%Y-%m-%d %H:%M:%S')
print(cday)

t = 1535348880.0
print('本地时间 ', datetime.fromtimestamp(t))
print('UTC时间 ', datetime.utcfromtimestamp(t))

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减 需要导入timedelta
# days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0
print('----日期加减---')
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now - timedelta(minutes=10))
print(now + timedelta(days=2, hours=12))
