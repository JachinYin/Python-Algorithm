# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 20
Author: Jachin
This is a scrpit for ...
'''
t = 0

Size = 4
b = [[0 for _ in xrange(Size)] for _ in xrange(Size)]
def board(size,tx,ty,dx,dy):
    global t
    if size == 1: return
    t = t + 1
    s = size / 2

    #1
    if dx < tx+s and dy < ty + s:
        board(s, tx,ty,dx,dy)
    else:
        b[dx+s-1][dy+s-1] = t
        board(s,tx,ty,dx+s-1,dy+s-1)

    #2
    if dx < tx+s and dy >= ty + s:
        board(s, tx,ty+s,dx,dy)
    else:
        b[dx+s-1][dy+s] = t
        board(s,tx,ty+s,dx+s-1,dy+s)

    #3
    if dx >= tx+s and dy < ty + s:
        board(s, tx+s,ty,dx,dy)
    else:
        b[dx+s][dy+s-1] = t
        board(s,tx+s,ty,dx+s,dy+s-1)

    if dx >= tx+s and dy >= ty + s:
        board(s, tx+s,ty+s,dx,dy)
    else:
        b[dx+s][dy+s] = t
        board(s,tx+s,ty+s,dx+s,dy+s)

board(Size,0,0,0,0)
for i in b:
    print i