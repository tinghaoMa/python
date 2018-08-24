#!/user/bin/python3
#  -*- coding: utf-8 -*-
'''
    Python内置的logging模块可以非常容易地记录错误信息

    raise 可以抛出一个错误类型 例如：ValueError TypeError

'''
import logging
import sys

# # 获取logger实例，如果参数为空则返回root logger
# logger = logging.getLogger("AppName")
#
# # 指定logger输出格式
# formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
#
# # 文件日志
# file_handler = logging.FileHandler("demo/error_exception/test.log")
# file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
#
# # 控制台日志
# console_handler = logging.StreamHandler(sys.stdout)
# console_handler.formatter = formatter  # 也可以直接给formatter赋值
#
# # 为logger添加的日志处理器
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)
#
# # 指定日志的最低输出级别，默认为WARN级别
# logger.setLevel(logging.WARN)
#
# # 输出不同级别的log
# logger.debug('this is debug info')
# logger.info('this is information')
# logger.warning('this is warning message')
# logger.error('this is error message')
# logger.fatal('this is fatal message, it is same as logger.critical')
# logger.critical('this is critical message')
#
# # try:
#     print('try...')
#     r = 10 / 0
#     print('result :', r)
# except ZeroDivisionError as e:
#     print('except: ', e)
# finally:
#     print('finally...')
# print('End Over')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        # logging.exception(e)
        raise ValueError('input error!')
    finally:
        print(' finally ....')


main()
