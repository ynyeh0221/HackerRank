#!/bin/python

import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
res = 0
for i in xrange(len(a)):
    for j in xrange(i+1, len(a)):
        if (a[i] + a[j]) % k == 0:
            res += 1
print res
