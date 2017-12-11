# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 06
Author: Jachin
直接插入排序
'''

from randomNumber import *


def insertionSort(arr):
    res = [arr[0]]  # 排好序的列表。默认第一个数是排序的了
    for i in range(1, len(arr)):
        if arr[i] > res[i - 1]:  # 如果要处理的数比res最后一个还大，则直接插到res末尾
            res.append(arr[i])
        else:
            for j in range(i):# 从已经排好序的数列res的第一个数开始
                if arr[i] <= res[j]:    #用要插入的数与res的数依次比较
                    res.insert(j, arr[i])#如果要插入的数比res中某个数小，则直接插入到这个数前
                    break
    return res

begin_time =  datetime.datetime.now()
print insertionSort(number_arr)
end_time =  datetime.datetime.now()

print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))
