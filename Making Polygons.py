#!/bin/python
import sys

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

if n == 1:
    print 2
res = 0
for i in a:
    if i >= sum(a)/2:
        res += 1
print res
