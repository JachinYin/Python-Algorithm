# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 18
Author: Jachin
This is a scrpit for ...
'''

mi = 21

def main():
    num = [i ** mi for i in range(10)]
    print'num Ok:',num
    cishu = [0 for _ in range(10)]
    fun(num, cishu, 0, 0)


def fun(num, cishu, m, n):
# m表示当前处理的是数组cishu的第几位
# n表示21位的名额已经甩掉了多少
    if (m == 9):
        cishu[9] = mi - n
        jisuan(num, cishu)
        return

        # 对当前位置所有可能进行枚举
    for i in range(mi - n):
        cishu[m] = i
        fun(num, cishu, m + 1, n + i)
        print cishu


def jisuan(num, cishu):
    ss = 0
    for i in range(10):
        ss += num[i] * cishu[i]

    if len(str(ss)) != mi:
        return

    cishu2 = [0 for _ in range(10)]

    # 确认和中各数字各出现多少次

    for i in range(mi):
        cishu2[int(str(ss)[i])] += 1

    # 测试数组cishu和数组cishu2是否完全匹配

    for i in range(10):
        if (cishu[i] != cishu2[i]):
            return

            # 完全匹配，打印结果
    print ss

main()
