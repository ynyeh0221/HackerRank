#!/bin/python

#pass 1-10 test cases, and got timeout on 11-16

from copy import deepcopy
import sys
import math
N = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

disk=[[] for y in range(4)]
ini=[[] for y in range(4)]

for i in xrange(N-1,-1,-1):
    disk[a[i]-1].append(i+1)
    ini[0].append(i+1)    

    
dic={}
ind=0
dic[0]=ini
ind+=1
z=0
visited={}
visited[','.join(map(str,ini))]=1
nextlevel={}
i=0
check=0
while i<=math.pow(2,N):
    for k in xrange(4):
        for j in xrange(4):
            temp=deepcopy(dic[z])
            if len(temp[k])!=0 and j!=k:
                move=temp[k].pop()
                if len(temp[j])==0 or (len(temp[j])!=0 and temp[j][len(temp[j])-1]>move):
                    temp[j].append(move)
                    kkey=','.join(map(str,temp))
                    if kkey not in visited:
                        dic[ind]=temp
                        visited[kkey]=1
                        nextlevel[ind]=1
                        ind+=1
                        if temp==disk:
                            print i+1
                            check=1
                            break
        if check==1:
            break
    if check==1:
        break
    del dic[z]
    z+=1
    if z in nextlevel:
        nextlevel={}
        i+=1
