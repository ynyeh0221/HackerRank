# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from operator import itemgetter

def Kruskal(V,mat):
    mstsum=0
    mat=sorted(mat,key=itemgetter(2))
    while (len(mat)>0):
        if mat[0][0] not in V[mat[0][1]-1] or mat[0][1] not in V[mat[0][0]-1]:
            V[mat[0][0]-1]=V[mat[0][0]-1] | V[mat[0][1]-1]
            V[mat[0][1]-1]=V[mat[0][0]-1]
            for i in V[mat[0][0]-1]:
                V[i-1]=V[mat[0][0]-1]
            mstsum+=mat[0][2]
        mat.pop(0)
    print mstsum

s=raw_input().split()
N=int(s[0])
M=int(s[1])
mat=[]
for m in xrange(M):
    s=map(int,raw_input().split())
    mat.append(s)
start=1
V=[]
for i in xrange(1,N+1):
    V.append(set([i]))
Kruskal(V,mat)
