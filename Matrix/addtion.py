# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 02
Author: Jachin
矩阵加法 
'''

import numpy as np

def Addition(matr1,matr2):
    if matr1 and matr2:
        if len(matr1)==len(matr1) and len(matr1[0])==len(matr2[0]):
            c = []
            for row in range(len(matr1)):
                r = []
                for column in range(len(matr1[0])):
                    r.append(matr1[row][column] + matr2[row][column])
                c.append(r)
            for i in  range(len(c)):
                print c[i]
        else:
            print "请输入行列一致的矩阵"
    else:
        print "请输入非空矩阵"

def Multipication(matr1,matr2):
    return np.multiply(matr1,matr2)

m1 = [[1,2],
      [2,5]
      ]
m2 = [[2,3],
      [4,9]
      ]

Addition(m1,m2)
print Multipication(m1,m2)


