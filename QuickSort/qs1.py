# -*- coding: utf-8 -*-
'''
快速排序
三路排序
Author: Jachin
Data: 2017- 11- 30
'''
from randomNumber import *  # 引入随机数列表生成模块

def quickSort(arr):
    '''
    快速排序算法1
    :param arr:实数的列表
    :return: 排序后的列表
    '''
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quickSort(less)
        more = quickSort(more)

        return less + pivotList + more

begin_time =  datetime.datetime.now()
quickSort(number_arr)
end_time =  datetime.datetime.now()

print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))
