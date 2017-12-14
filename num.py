# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 
Author: Jachin
This is a scrpit for ...
'''

from datetime import *

def waNum(mi):
    for number in xrange(10**(mi-1),10**mi):
        sum = 0
        for each in str(number):
            sum += int(each)**mi
        if sum == number:
            print number

def waNum2(mi):
    '''
    水仙花数，暴力解法。
    :param mi:要求解的位数
    :return:
    '''
    number = 10 ** (mi - 1)
    while number < 10**mi:
        sum = 0
        for each in str(number):
            sum += int(each)**mi
            if sum > number:
                break
        if sum == number:
            print number
        number += 1


def waNum3(mi):

    for number in xrange(10**(mi-1),10**mi):
        sum = 0
        res = []
        d = [0 for _ in range(10)]
        for i in str(number):
            d[int(i)] += 1
        d.pop(0)
        res.append(d)
    res = list(set(res))

    for i in range(len(res)):
        temp = res[i]


    for number in res:
        for i in xrange(9):
            if d[8-i] != 0:
                sum += d[8-i]*((9-i)**mi)
            if sum > number:
                break

        if sum == number:
            print number

begin = datetime.now()
#waNum2(4)
end = datetime.now()
print '2:用时%sS' %(str((end-begin).total_seconds()))

begin = datetime.now()
#waNum3(6)
end = datetime.now()
print '3:用时%sS' %(str((end-begin).total_seconds()))


a = [[0,1],[1,0],[0,1]]
if a[0]== a[2]:
    del a[2]
    print a