# -*- coding: utf-8 -*-
'''
产生随机数组
Author: Jachin
Data: 2017- 11- 27
'''

import datetime
import random

LENGTH = 10000 #生成随机数个数
BEGIN , END= -10,10 #生成随机数的范围取值

test_arr = [random.randint(BEGIN, END) for i in range(LENGTH)]

#test_arr = [1,2,-1,-3,5,-3,8]

#test_arr = [-1,2,-5,2,8]