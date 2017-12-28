# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 20
Author: Jachin
二叉树
'''
from math import sqrt

class BinTree:
    def __init__(self):
        pass
        self.leng = 1
        self.root = [0]
        self.hight = 1


    def build(self):
        pass

    def lChild(self):
        pass

    def rChild(self):
        pass

    def insert(self,num):
        #TODO insert chilldren
        if self.leng == 1 or self.leng == 2:
            self.root.append([num])
            self.leng += 1
        self.hight = sqrt(self.leng+1)

t = BinTree()
t.insert(2)
t.insert(7)
t.insert(8)
print t.hight
print t.leng
print t.root
