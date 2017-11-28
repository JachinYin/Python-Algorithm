# -*- coding: utf-8 -*-
'''
最大子段和问题的 分治算法
Author: Jachin
Data: 2017- 11- 28
'''
from randomNumber import *

pro = 0
las = 0
def maxSunSum(left,right):
    global pro,las
    sum = 0
    if left == right:
        if test_arr[left] > 0:
            sum = test_arr[left]
        else:
            sum = 0
    else:
        center = (left + right)//2
        leftSum = maxSunSum(left,center)        #情况1
        rightSum = maxSunSum(center+1,right)    #情况2
        #情况3
        s1 = 0
        lefts = 0
        for i in range(center,left-1,-1):
            lefts += test_arr[i]
            if lefts > s1:
                s1 = lefts
        s2 = 0
        rights = 0
        for j in range(center+1,right+1):
            rights += test_arr[j]
            if rights > s2:
                s2 = rights
        sum = s1+s2
        if sum < leftSum:
            sum = leftSum
        if sum < rightSum:
            sum = rightSum

        # if sum < leftSum :#and leftSum > rightSum:
        #     sum = leftSum
        #     pro = left
        #     las = center
        # if sum > leftSum and sum > rightSum:
        #     pro = i+1
        #     las = j-1
        # else:
        #     sum = rightSum
        #     pro = center + 1
        #     las = j+1
        
        
        
    return sum

begin_time =  datetime.datetime.now()
print '最大子段和:' + str(maxSunSum(0,len(test_arr)-1))
end_time =  datetime.datetime.now()

#print '从第 %d 个数到 第 %d 个数'%(pro,las)

print '算法用时%sS' %str((end_time-begin_time).total_seconds())