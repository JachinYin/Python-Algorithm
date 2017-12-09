# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 09
Author: Jachin
基数排序，只能对非负整数进行排序
'''

from randomNumber import *

def getNum(r,num):
    '''
    判断给定数字的某一位是几，比如435的第1位是5,第2位是3，第3位是4，第4位是0
    :param r: 指定数字的位数
    :param num: 给定的数字
    :return: 要查询的数字
    '''
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

    if r == len(str(max(arr))):
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



radixSort([12,45,34,41,999])
print result

begin_time =  datetime.datetime.now()
radixSort(number_arr)
end_time =  datetime.datetime.now()

print '排列%d个数用时%sS' %(len(number_arr),str((end_time-begin_time).total_seconds()))
