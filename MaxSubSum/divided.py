# -*- coding: utf-8 -*-
'''
最大子段和问题的 分治算法
Author: Jachin
Data: 2017- 11- 28
'''
from randomNumber import *

pro = 0
las = 0
def maxSubSum(left, right):
    global pro,las
    sum = 0
    if left == right:
        if number_arr[left] > 0:
            sum = number_arr[left]
        else:
            sum = 0
    else:
        center = (left + right)//2
        leftSum = maxSubSum(left, center)        #情况1
        rightSum = maxSubSum(center + 1, right)    #情况2
        #情况3
        s1 = 0
        lefts = 0
        for i in range(center,left-1,-1):
            lefts += number_arr[i]
            if lefts > s1:
                s1 = lefts
                pro = i
        s2 = 0
        rights = 0
        for j in range(center+1,right+1):
            rights += number_arr[j]
            if rights > s2:
                s2 = rights
                las = j
        #返回左边，右边，跨中间 的最大的一个值
        sum = max(s1+s2,leftSum,rightSum)
    return sum

begin_time =  datetime.datetime.now()
print '最大子段和:' + str(maxSubSum(0, len(number_arr) - 1))
end_time =  datetime.datetime.now()

print '从第 %d 个数到 第 %d 个数'%(pro+1,las+1)

print '算法用时%sS' %str((end_time-begin_time).total_seconds())

