#!/user/bin/python3
#  -*- coding: utf-8 -*-
from urllib import request

# GET请求
# url = 'http://edu.tv.sohu.com/sdk/clockDetail.do?roomId=1815'
# with request.urlopen(url) as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s  :~     %s' % (k, v))
#     print('Data :', data.decode('utf-8'))


req = request.Request('http://www.baidu.com/')
req.add_header('User-Agent',
               'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D)'
               'AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166'
               '  Safari/535.19')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
