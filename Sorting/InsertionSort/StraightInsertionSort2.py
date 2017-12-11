# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 11
Author: Jachin
直接插入排序，更简单的写法
'''
from randomNumber import *

def insertSort2(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            temp = arr[i]
            arr[i] = arr[i-1]
            j = i-1
            while temp < arr[j] and j >= 0:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp
    return arr



# A = [49,38,65,97,26,13,27,49,55,4]
# print insertSort2(A)

begin_time =  datetime.datetime.now()
insertSort2(number_arr)
end_time =  datetime.datetime.now()

print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))
