# -*- coding: utf-8 -*-
'''
产生随机数组
Author: Jachin
Data: 2017- 11- 27
'''

import datetime
import random

LENGTH = 20000 #生成随机数个数
BEGIN , END= 0,100000 #生成随机数的范围取值

number_arr = [random.randint(BEGIN, END) for i in range(LENGTH)]
