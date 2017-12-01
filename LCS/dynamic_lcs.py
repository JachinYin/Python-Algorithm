# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 1
Author: Jachin
最长公共子序列问题
'''

def LCS(x,y):
    '''
    返回最长公共子序列的长度
    '''
    x = "1" + x
    y = "2" + y
    c = [[0 for i in range(len(y))] for j in range(len(x))]
    b = [['→' for i in range(len(y))] for j in range(len(x))]
    for i in range(1,len(x)):
        for j in range(1,len(y)):
            if x[i]==y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "↘"
            elif c[i-1][j]>= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "↓"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "→"

    s = []

    def lcsPut(i,j,x,b):
        if i==0 and j==0:
            return
        if i<0 or j< 0:
            return
        if b[i][j] == '↘':
            lcsPut(i - 1, j - 1, x, b)
            s.append(x[i])
        elif b[i][j] == '↓':
            lcsPut(i-1, j, x, b)
        else:
            lcsPut(i, j - 1, x, b)




    leng = c[len(x)-1][len(y)-1]
    if leng:
        # for i in c:
        #     print i
        lcsPut(len(x)-1,len(y)-1,x,b)
        print "最长公共子序列为%s"%(''.join(s))
        print "其长度为：%d"%leng
        print "数组c"
        for i in b:
            print " ".join(i)
        #print b#"最长公共子序列为：%s"%"".join(b)
    else:
        print "没有公共子序列。"

x = raw_input("Input string 1:\n")
y = raw_input("Input string 2:\n")

LCS(x,y)