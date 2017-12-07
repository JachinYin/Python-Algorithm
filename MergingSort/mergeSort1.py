# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 07
Author: Jachin
归并排序
'''
from randomNumber import *

def megeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)/2
    left = megeSort(arr[:mid])
    right = megeSort(arr[mid:])

    i = 0  # left 计数
    j = 0  # right 计数
    k = 0  # 总计数

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    remain = left if i < j else right
    r = i if remain == left else j

    while r < len(remain):
        arr[k] = remain[r]
        r += 1
        k += 1

    return arr

test_arr = [1,4,3,2,7,9]
#print megeSort(test_arr)

begin_time =  datetime.datetime.now()
megeSort(number_arr)
end_time =  datetime.datetime.now()

print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))
