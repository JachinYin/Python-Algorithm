# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 06
Author: Jachin
插入排序
'''
from randomNumber import *
import datetime  # 引入该模块统计算法运行时间


def insertionSort(arr):
    res = [arr[0]]  # 排好序的列表。默认第一个数是排序的了
    for i in range(1, len(arr)):
        if arr[i] > res[i - 1]:  # 如果要处理的数比res最后一个还大，则直接插到res末尾
            res.append(arr[i])
        else:  # 否则判断
            for j in range(i):
                if arr[i] <= res[j]:
                    # 从排序的第一个数（记为a）开始，如果要处理的数比a小，则直接插入，否则向后比较
                    res.insert(j, arr[i])
                    break
    return res


test_arr = [22, 4, 1, 29, 7, 3, 5, 9, 88]



begin_time =  datetime.datetime.now()
insertionSort(number_arr)
end_time =  datetime.datetime.now()

print '算法用时 %sS' %str((end_time-begin_time).total_seconds())
