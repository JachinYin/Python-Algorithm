# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 04
Author: Jachin
活动安排问题
贪心算法
'''

def quickSort(arr):
    '''
    快速排序算法,将活动的时间按照最早结束的顺序排列
    :param arr:元素为二元元组的列表如:arr=[(3,5),(1,7),(4,8)]
    :return: 结束时间升序的一个活动表
    '''
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0][1]
        for i in arr:
            if i[1] < pivot:
                less.append(i)
            elif i[1] > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quickSort(less)
        more = quickSort(more)

        return less + pivotList + more


def greedySelector2(s, f):
    '''

    :param s: list，每一个活动的开始时间
    :param f: list，排好序的结束时间
    :return:
    '''
    d = list(zip(s, f))
    schedule = quickSort(d)
    print ("活动编号从1起排列如下(一行5个)")
    count  = 0
    for i in schedule:
        print i,
        count += 1
        if count % 5 == 0:
            print
    print("\n")
    n = len(schedule)
    j = 0
    a = [1]
    for i in range(n):
        if schedule[i][0] >= schedule[j][1]:
            a.append(i + 1)
            j = i
    return a

s = [4, 1, 3, 0, 5, 3, 5,  6,  8,  8,  2, 12]
f = [5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

result = greedySelector2(s, f)

print("举行的活动有%d个，编号是%s"%(len(result),str(result)))