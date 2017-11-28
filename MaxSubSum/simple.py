# -*- coding: utf-8 -*-
'''
最大子段和问题的 简单解法
Author: Jachin
Data: 2017- 11- 
'''
from randomNumber import *

pro = 0
las = 0
def Maxsum(s):
    '''
    simple for max sub sum
    :param s:
    :return sum:
    '''
    global pro,las
    sum = 0
    for i in range(len(s)):
        thisissu = 0
        #如果s[i]<0，下面的循环可以跳过

        for j in range(i,len(s)):
            thisissu += s[j]
            if thisissu>sum:
                sum = thisissu
                pro = i
                las = j
    return sum

#print '原数组为 %s'%s

begin_time =  datetime.datetime.now()
print '最大子段和:' + str(Maxsum(test_arr))
end_time =  datetime.datetime.now()

print '从第 %d 个数到 第 %d 个数'%( pro+1,las+1)

print '算法用时%sS' %str((end_time-begin_time).total_seconds())
