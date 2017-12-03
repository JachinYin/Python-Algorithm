# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 03d
Author: Jachin
二分搜索
'''

from randomNumber import *

def quickSort(L):
    if not L:
        return []
    else:
        pivot = random.choice(L)
        less = [x for x in L if x < pivot]
        more = [x for x in L[1:] if x > pivot]
        return quickSort(less) + [pivot]*L.count(pivot) + quickSort(more)

def binarySearch(arr,num):
    left,right = 0,len(arr)
    while left<=right:
        middle = (left+right)//2
        if num == arr[middle]:
            return middle
        if num > arr[middle]:
            left = middle +1
        else :
            right = middle-1
    return -1

#获取一个随机数组，并排序
num = quickSort(number_arr)

#输出所查找数的下标，没有该数则输出-1
print binarySearch(num,22)
