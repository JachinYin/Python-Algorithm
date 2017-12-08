# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 08
Author: Jachin
冒泡排序
'''

from randomNumber import *

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[j]<arr[j-1]:
                arr.insert(j-1,arr.pop(j))
    return arr

print bubbleSort([1,4,3,6,7])

begin_time =  datetime.datetime.now()
bubbleSort(number_arr)
end_time =  datetime.datetime.now()

print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))


