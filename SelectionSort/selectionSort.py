# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 08
Author: Jachin
选择排序，每次选出最大或最小值
'''
from randomNumber import *

def selectionSort(arr):
    '''
    选择排序
    '''
    res = []
    for i in range(len(arr)):
       res.append(min(arr))
       arr.remove(min(arr))
    return res


test_arr = [1,4,3,2,5,4,6]

print(selectionSort(test_arr))

begin_time =  datetime.datetime.now()
number_arr = selectionSort(number_arr)
end_time =  datetime.datetime.now()

print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))
