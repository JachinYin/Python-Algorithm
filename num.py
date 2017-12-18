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
    temp = []
    num = 10 ** (mi - 1)
    while num < 10**mi:
        d = [0 for _ in range(10)]
        for i in str(num):
            d[int(i)] += 1
        d.pop(0)
        if d not in temp:
            temp.append(d)
        num += 1
        if num % (10**(mi-1)) == 0:
            print num

    for number in temp:
        fire = 0
        for i in xrange(9):
            fire += number[i] * (i+1)**mi
        if len(str(fire)) == mi:
            d = [0 for _ in range(10)]
            for i in str(fire):
                d[int(i)] += 1
            d.pop(0)
            if number == d:
                print fire

def waNum4(mi):
    mi_res = [i**mi for i in range(10)]
    #print mi_res
    for i in range(mi):
        for num in mi_res:
            pass
            #print i



def waNum5(mi):
    temp = []
    num = 10 ** (mi - 1)
    while num < 10**mi:
        d = [0 for _ in range(10)]
        for i in str(num):
            d[int(i)] += 1
        d.pop(0)
        temp.append(d)
        num += 1

    res = []
    for i in temp:
        if i not in res:
            res.append(i)

    print len(temp),len(res)


#waNum5(5)



begin = datetime.now()
#waNum2(5)
end = datetime.now()
print '2:用时%sS' %(str((end-begin).total_seconds()))

begin = datetime.now()
#waNum3(6)
#waNum4(21)
end = datetime.now()
print '3:用时%sS' %(str((end-begin).total_seconds()))



import pprint
root = [[[0,1,2],[0,1],2],[[0,1,2],[0,1]],2]
