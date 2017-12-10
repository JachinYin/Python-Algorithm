# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 10
Author: Jachin
基数排序更简单的写法
'''

from random import randint
from randomNumber import *

def radixSort(arr,digit = 5):
    '''
    基数排序，对非负整数进行排序
    :param arr: 无序数列
    :param digit: 数列中数字的最高位数,默认最高5位数
    :return: 排好序的数列
    '''
    for d in xrange(digit):
        buckets = [[] for _ in xrange(10)]
        for num in arr:
            #对数字进行入桶操作
            buckets[num / (10 ** d) % 10].append(num)
            #把拼接桶后的数列直接赋值给arr，
            # 下一轮循环时，就是已经整理一次的数列了
            arr = [item for buc in buckets for item in buc]
    return arr

begin_time =  datetime.datetime.now()
print radixSort(number_arr,len(str(max(number_arr))))
end_time =  datetime.datetime.now()

print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))


