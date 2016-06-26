#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
res = sys.maxint
dic = {}
for i in xrange(n):
    if A[i] not in dic:
        dic[A[i]] = i
    else:
        res = min(res, i - dic[A[i]])
        dic[A[i]] = i
print res if res < sys.maxint else -1
