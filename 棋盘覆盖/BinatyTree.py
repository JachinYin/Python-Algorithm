# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 20
Author: Jachin
二叉树
'''
from math import sqrt

class Node():
    '''节点类'''
    def __init__(self,elem = -1,lchild = None,rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class BinTree:
    def __init__(self):
        #TODO build initial tree
        self.root = Node()
        self.myQueue = []

    def add(self,elem):
        #TODO add Node to a tree
        pass
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root is None:
            return
        print root.elem,
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

t = BinTree()
t.add(3)
t.add(2)
t.add(5)
t.add(7)
t.front_digui(t.root)

