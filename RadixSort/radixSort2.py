# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 10
Author: Jachin
基数排序
'''

from randomNumber import *
# import sys
# sys.setrecursionlimit(10000)

def getR(arr):
    '''
    获取最高位数
    :param arr: 数列
    :return: 数列中的最高位数
    '''
    if arr[0]<0:
        return len(str(min(arr)))
    if arr[0]>0:
        return len(str(max(arr)))

def getNum(r,num):
    '''
    判断给定数字的某一位是几
    比如435的第1位是5,第2位是3，第3位是4，第4位是0
    :param r: 指定数字的位数
    :param num: 给定的数字
    :return: 要查询的数字
    '''

    if str(num)[0] == '-':
        s = str(num)[1:]
        leng = len(s)
        if leng - r < 0:
            return 0
        else:
            return int(s[leng - r])

    else:
        leng = len(str(num))
        if leng-r < 0:
            return 0
        else:
            return int(str(num)[leng-r])


result = []     #保存排序的结果
def radixSort(arr,r=1):
    global result
    d = dict(zip([i for i in range(10)],[[] for i in range(10)]))   #指定0-9十个桶
    res = []    #将0-9个桶的数依次装入res

    if r == getR(arr):
        #递归出口，如果位数为当前数列中的数字的最高位，则表明已经完成排序，返回结果
        for item in arr:
            d[getNum(r,item)].append(item)  #将相应的数字装进对应的桶
        for v in d.values():
            res += v
        result =  res

    else:
        for item in arr:
            d[getNum(r,item)].append(item)  #将相应的数字装进对应的桶
        for v in d.values():
            res += v
        radixSort(res,r+1)


def positive_negetive(arr):
    '''
    处理正负数
    :param arr: 源序列
    :return: 返回排序后的结果
    '''
    global result
    arr1 = []   #保存负数
    arr2 = []   #保存正数
    results = []    #返回最终的排序结果
    for item in arr:
        if item < 0:    #负数则添加进arr1
            arr1.append(item)
        else:           #正数添加进arr2
            arr2.append(item)
    if arr1:    #如果有负数
        radixSort(arr1)
        results=result[::-1]    #将负数列表逆转后保存到results中
    if arr2:    #如果有正数
        radixSort(arr2)
        results += result       #将负数部分和正数部分结合
    return results





print positive_negetive([-1,-12,-45,-34,-41,-999,-99,4,0,6,8])

#print positive_negetive([-99,-899,-199,-29,4])

# begin_time =  datetime.datetime.now()
# positive_negetive(number_arr)
# end_time =  datetime.datetime.now()
#
# print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))
#
