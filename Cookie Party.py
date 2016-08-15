#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]

if m % n == 0:
    print 0
elif n > m:
    print n - m
elif n < m:
    print n - m % n
