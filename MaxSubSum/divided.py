# -*- coding: utf-8 -*-
'''
This is a scrpit for ...
Author: Jachin
Data: 2017- 11- 28
'''
from randomNumber import *

def maxSunSum(left,right):
    sum = 0
    if left == right:
        if test_arr[left] > 0:
            sum = test_arr[left]
        else:
            sum = 0
    else:
        center = (left + right)//2
        leftSum = maxSunSum(left,center)
        rightSum = maxSunSum(center+1,right)
        s1 = 0
        lefts = 0
        for i in range(center,left-1,-1):
            lefts += test_arr[i]
            if lefts > s1:
                s1 = lefts
        s2 = 0
        rights = 0
        for i in range(center+1,right+1):
            rights += test_arr[i]
            if rights > s2:
                s2 = rights
        sum = s1+s2
        if sum < leftSum:
            sum = leftSum
        if sum < rightSum:
            sum = rightSum
    return sum

print maxSunSum(1,len(test_arr)-1)
        