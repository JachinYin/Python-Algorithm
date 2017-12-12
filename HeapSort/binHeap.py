# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 12
Author: Jachin
数据结构:二叉堆
使用列表形式来存储二叉堆
列表首位永远为0，不属于堆的元素，仅为了方便节点的管理
父节点下标为P，则左孩子为2p，右孩子为2p+1
'''
class BinHeap(object):
    '''
    二叉堆，最小堆。方法有：
    创建堆buildHeap()，插入节点insert()，删除最小节点delMin()
    其他的方法bubbleUp(),bubbleDown(),minChild()都是辅助前面三个方法的
    '''
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def bubbleUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,num):
        self.heapList.append(num)
        self.currentSize = self.currentSize + 1
        self.bubbleUp(self.currentSize)
        pass

    def bubbleDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.bubbleDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.bubbleDown(i)
            i = i - 1
