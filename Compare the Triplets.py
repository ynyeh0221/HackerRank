#!/bin/python

import sys


a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

score=[0,0]

if a0>b0:
    score[0]+=1
elif a0<b0:
    score[1]+=1
if a1>b1:
    score[0]+=1
elif a1<b1:
    score[1]+=1
if a2>b2:
    score[0]+=1
elif a2<b2:
    score[1]+=1
print " ".join(str(e) for e in score)
