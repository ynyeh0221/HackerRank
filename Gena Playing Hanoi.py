#!/bin/python

# It passes 1-10 test case, but gets timeout on 11-16

from copy import deepcopy
import sys
import math
N = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

end=[[] for y in range(4)] # end state
initial=[[] for y in range(4)] # initial state

for i in xrange(N-1,-1,-1):
    end[a[i]-1].append(i+1)
    initial[0].append(i+1)    
    
states={} # the states to be check
states[0]=initial

visited={} # the states already visited
visited[','.join(map(str,initial))]=1

nextlevel={} # the next level states

i=0
z=0
ind=1
check=0

while i<=math.pow(2,N): # maximum steps
    for k in xrange(4):
        for j in xrange(4):
            temp=deepcopy(states[z])
            if len(temp[k])!=0 and j!=k:
                move_disk=temp[k].pop()
                if len(temp[j])==0 or (len(temp[j])!=0 and temp[j][len(temp[j])-1]>move_disk):
                    temp[j].append(move_disk)
                    kkey=','.join(map(str,temp))
                    if kkey not in visited:
                        states[ind]=temp
                        visited[kkey]=1 # don't save duplicate states
                        nextlevel[ind]=1 # the next level states
                        ind+=1
                        if temp==end:
                            print i+1
                            check=1
                            break
        if check==1:
            break
    if check==1:
        break
    del states[z]
    z+=1
    if z in nextlevel:
        nextlevel={}
        i+=1
