#!/bin/python
import sys

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

if n == 1:
    print 2
elif n == 2:
    if a[0] == a[1]:
        print 2
    else:
        print 1
elif n >= 3:
    if sum(a) <= 2 * max(a):
        print 1
    else:
        print 0
