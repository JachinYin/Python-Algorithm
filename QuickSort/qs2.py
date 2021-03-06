# -*- coding: utf-8 -*-
'''
快速排序算法2
三路排序
选择列表中的随机一个数做基准,基本保证了算法的时间复杂的稳定在nlogn层次
Author: Jachin
Data: 2017- 11- 30
'''

from randomNumber import *  # 引入随机数列表生成模块


def quickSort(L):
    if not L:
        return []
    else:
        pivot = random.choice(L)
        less = [x for x in L if x < pivot]
        more = [x for x in L[1:] if x > pivot]
        return quickSort(less) + [pivot]*L.count(pivot) + quickSort(more)

begin_time =  datetime.datetime.now()
quickSort(number_arr)
end_time =  datetime.datetime.now()

print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))
