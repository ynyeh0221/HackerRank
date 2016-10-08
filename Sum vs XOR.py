#!/bin/python

import sys

n = long(raw_input().strip())
binn = bin(n)[2:]
res = 0
zeros = 0
for i in xrange(len(binn)-1, -1, -1):
    if binn[i] == '0':
        zeros += 1
print 2 ** zeros if n > 0 else 1
