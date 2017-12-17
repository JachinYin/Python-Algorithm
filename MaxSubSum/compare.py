# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 17
Author: Jachin
比较三个算法的时间复杂度，并作图表示
'''

from simple import *
from divided import *
from dynamic import *

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

# plt.rcParams['font.sans-serif'] = ['SimiHei']
# plt.rcParams['axes.unicode_minus'] = False

def drawPlot(xData, yData, d):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 柱状图
    ax.set_title('Time comparison')
    ax.bar(xData, yData, facecolor='#9999ff', edgecolor='white', align='center')

    # 显示数字
    for x, y in zip(xData, yData):
        ax.text(x, y, y, ha='center', va='bottom')

    xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为1的倍数
    ax.xaxis.set_major_locator(xmajorLocator)
    # ax.yaxis.set_major_locator(xmajorLocator)
    plt.xlim(0.5 ,3.5)

    # 设置坐标轴信息
    plt.xtext = plt.xlabel(u'3 kinds of Algorithms')
    plt.ytext = plt.ylabel(u'Time(S)')

    # 出现网格
    plt.grid(True)

    plt.show()

s = [1,2,3]
t = [time1,time2,time3]
drawPlot(s, t, 2017)
