# -*- coding: utf-8 -*-
'''
最大子段和问题 动态规划解法
Author: Jachin
Data: 2017- 11- 29
'''

from randomNumber import *

pro = 0
las = 0

def maxSubSum(s):
    global pro,las
    thisSum = 0
    maxSum = 0
    for i in range(len(s)):
        thisSum += s[i]
        if(thisSum > maxSum):
            maxSum = thisSum
            las = i
        elif thisSum < 0:
            thisSum = 0
            pro = i+1

    return maxSum


begin_time =  datetime.datetime.now()
print '最大子段和:' + str(maxSubSum(test_arr))
end_time =  datetime.datetime.now()

print '从第 %d 个数到 第 %d 个数'%(pro+1,las+1)

print '算法用时%sS' %str((end_time-begin_time).total_seconds())

