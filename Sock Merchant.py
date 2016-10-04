#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
dic = {}
res = 0
for i in c:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1
for i in dic:
    res += dic[i] / 2
print res
