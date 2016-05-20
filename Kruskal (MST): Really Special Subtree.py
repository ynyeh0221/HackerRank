# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from operator import itemgetter
from sets import Set

def Kruskal(V,adj,mat):
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
adj=[[-1 for i in range(N)] for j in range(N)]
for i in range(N):
    adj[i][i]=0
mat=[]
for m in xrange(M):
    s=raw_input().split()
    x=int(s[0])
    y=int(s[1])
    r=int(s[2])
    adj[x-1][y-1]=r
    adj[y-1][x-1]=r
    s=map(int,s)
    mat.append(s)
start=int(raw_input())
V=[]
for i in xrange(1,N+1):
    V.append(set([i]))
Kruskal(V,adj,mat)
