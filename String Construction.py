#!/bin/python

import sys


n = int(raw_input().strip())
for a0 in xrange(n):
    s = raw_input().strip()
    res = 0
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
            res += 1
    print res
