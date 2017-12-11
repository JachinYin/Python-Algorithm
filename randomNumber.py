# -*- coding: utf-8 -*-
'''
产生随机数组
Author: Jachin
Data: 2017- 11- 27
'''

import datetime
import random

number_arr = []
def getArray(LENGTH = 10000,BEGIN = -1000, END = 1000):
    '''
    生成随机数列
    :param LENGTH: 生成随机数个数
    :param BEGIN: 生成的随机数的最小值
    :param END:  生成的随机数的最大值
    :return:
    '''
    global number_arr
    number_arr = [random.randint(BEGIN, END) for i in range(LENGTH)]
    return number_arr

getArray()