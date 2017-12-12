# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 11
Author: Jachin
This is a scrpit for Shell's sort
'''

def shellSort1(arr):
    gap = len(arr)/2
    if gap == 1:
        return arr


def shellSort(arr):
    n = len(arr)
    gap = n / 2
    while gap > 0:
        gap = gap / 2
        for j in range(gap,n):
            if (arr[j] < arr[j - gap]):# // 每个元素与自己组内的数据进行直接插入排序
                temp = arr[j]
                k = j - gap
                while k >= 0 and arr[k] > temp:

                    arr[k + gap] = arr[k]
                    k -= gap
                    arr[k + gap] = temp
    return arr

A = [49,38,65,97,26,13,27,49,55,4]

print shellSort(A)