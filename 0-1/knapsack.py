# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 05
Author: Jachin
0-1背包问题。
'''



def knapsack(w,v,c):
    '''
    求解0-1背包问题，最后得到背包最大价值
    :param w: 每一个物品的重量
    :param v: 每一个物品的价值
    :param c: 背包的最大容量
    :return: 背包的最大价值
    '''
    w.insert(0,0)       #为方便计算，把它变为w = [0，2,3,4,5,9]
    v.insert(0,0)       #为方便计算，把它变为v = [0，3,4,5,8,10]
    #相应的，c自增1
    c += 1
    #物品个数+1
    n = len(w)
    B = [[0 for i in range(c)] for i in range(n)]
    for item in range(n):
        for weight in range(c):
            if w[item] > weight:    #如果当前物品过重
                B[item][weight] = B[item-1][weight]
            else:   #否则比较当前物品装进背包前后的大小，取大者
                B[item][weight] = max(B[item-1][weight-w[item]]+v[item],
                                      B[item-1][weight])


    #for i in B:
        #print i
    return B

def traceback(w,c,m):

    n = len(w)
    x =[0 for q in range(n)]
    for i in range(n-1,0,-1):
        #如果把当前价值的最后一个物品去掉，价值变小，
        # 说明这个物品是被添加到背包里的
        if m[i][c]>m[i-1][c]:
            x[i] = 1
            c -= w[i]
        else:   #否则不添加进背包
            x[i]=0

    x.pop(0)

    res = []        #记录添加的物品的编号
    for i in range(len(x)):
        if x[i]:
            res.append(i+1)
    return res

c = 20  #背包容量

w = [2,3,4,5,9] #各物品重量
v = [3,4,5,8,10]    #各物品价值

#v = [1,3,5,9]
#w = [2,3,4,7]

count = 0
for i in zip(w,v):
    count += 1
    print("物品%-2d，重量：%d,价值：%d"%(count,i[0],i[1]))

re = knapsack(w,v,c)
print("这个背包取得的最大价值为【%d】" % re[-1][-1])

print("装入物品的编号为%s"%str(traceback(w,c,re)))
