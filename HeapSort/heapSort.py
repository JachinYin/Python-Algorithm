# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 12
Author: Jachin
堆排序
就是从二叉堆(最小堆)中取出最小值(首元素)，堆自动会进行调整，然后循环取最小值，直到堆为空
所有取出的最小值便形成了升序数列
创建堆所需时间O(n),取最小值为O(1),堆调整为O(logn)，总时间O(nlogn)
'''
from randomNumber import *
from binHeap import *

def heapSort(arr):
    bh = BinHeap()
    bh.buildHeap(arr)
    res = []
    while bh.currentSize >0:
        res.append(bh.heapList[1])
        bh.delMin()
    return res

# A = [49,38,65,97,26,13,27,53,55,4]
# print heapSort(A)

begin_time =  datetime.datetime.now()
heapSort(getArray(100000,-10000,10000))
end_time =  datetime.datetime.now()

print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))
