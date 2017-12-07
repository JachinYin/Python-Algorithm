# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 07
Author: Jachin
This is a scrpit for ...
'''

from randomNumber import *

def merge(left, right):
    '''
    合并两个已经排好序的列表
    :param left: 左边有序的列表
    :param right: 右边有序的列表
    :return: 返回排序后的列表
    '''
    merged = [] #合并后有序的列表

    while left and right:
        #比较两边排好序的列表的第一个数，小的就加入merge，同时把这个数从原列表删除
        #直到其中一个列表为空或两个列表都为空
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

    while left:
        #如果是右边部分为空的，则将左边列表直接加入merge的末尾
        merged.append(left.pop(0))

    while right:
        #如果是左边部分为空的，则将右边列表直接加入merge的末尾
        merged.append(right.pop(0))

    return merged   #返回排好序的列表

def megeSort(arr):
    if len(arr) == 1:   #递归出口，列表被分得剩下一个数时，就已经排好序了
        return arr

    mid = len(arr)/2    #分
    left = megeSort(arr[:mid])  #左边继续分下去
    right = megeSort(arr[mid:]) #右边继续分下去

    return merge(left,right)    #将排好序的两个部分合并到一起



test_arr = [1,4,3,2,7,9]
#print megeSort(test_arr)

begin_time =  datetime.datetime.now()
megeSort(number_arr) #调用随机生成的列表
end_time =  datetime.datetime.now()

print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))
