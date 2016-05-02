#!/bin/python

import sys


n = int(raw_input().strip())
B = map(int, list(raw_input().strip()))

count=0
for i in xrange(2,n):
    if B[i-2]==0 and B[i-1]==1 and B[i]==0:
        B[i]=1
        count+=1
print count
