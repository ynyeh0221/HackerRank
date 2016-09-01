#!/bin/python

import sys


a0,a1,a2 = raw_input().strip().split(' ')
a = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]

A =B =0
for i in xrange(3):
    if a[i] > b[i]:
        A += 1
    elif a[i] < b[i]:
        B += 1
print str(A) + ' ' + str(B)
