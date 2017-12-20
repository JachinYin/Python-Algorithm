# -*- coding: utf-8 -*-
'''
Data: 2017- 12 - 20
Author: Jachin
This is a scrpit for ...
'''

def board(size, tx, ty, dx, dy):
    global t1, b
    if size == 1: return
    t1 = t1 + 1
    t = t1
    s = size // 2

    # 1
    if dx < tx + s and dy < ty + s:
        board(s, tx, ty, dx, dy)
    else:
        b[tx + s - 1][ty + s - 1] = t
        board(s, tx, ty, tx + s - 1, ty + s - 1)

    # 2
    if dx < tx + s and dy >= ty + s:
        board(s, tx, ty + s, dx, dy)
    else:
        b[tx + s - 1][ty + s] = t
        board(s, tx, ty + s, tx + s - 1, ty + s)

    # 3
    if dx >= tx + s and dy < ty + s:
        board(s, tx + s, ty, dx, dy)
    else:
        b[tx + s][ty + s - 1] = t
        board(s, tx + s, ty, tx + s, ty + s - 1)

    # 4
    if dx >= tx + s and dy >= ty + s:
        board(s, tx + s, ty + s, dx, dy)
    else:
        b[tx + s][ty + s] = t
        board(s, tx + s, ty + s, tx + s, ty + s)


t1 = 0
Size = 16

b = [[0 for _ in xrange(Size)] for _ in xrange(Size)]


board(Size, 0, 0, 0, 2)
for i in b:
    print i
