# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 04
Author: Jachin
活动安排问题
贪心算法
'''


def greedySelector(s, f):
    '''

    :param s: list，每一个活动的开始时间
    :param f: list，排好序的结束时间
    :return:
    '''
    n = len(s)
    j = 1
    a = [1]
    for i in range(1, n):
        if s[i] >= f[j]:
            a.append(i + 1)
            j = i
    return a


s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

result = greedySelector(s, f)

print("举行的活动有%d个，编号是%s"%(len(result),str(result)))