# Enter your code here. Read input from STDIN. Print output to STDOUT
#prim algorithm, 4, 5, 6 timeout

import sys

def prim(mst,V,adj):
    mstsum=0
    while (len(mst)<N):
        minn=sys.maxint
        v=-1
        edges=[]
        for i in mst:
            for j in V:
                if adj[i-1][j-1]>0:
                    if minn>adj[i-1][j-1]:
                        minn=adj[i-1][j-1]
                        v=j
        mstsum+=minn
        mst.append(v)
        V.remove(v)
    print mstsum

s=raw_input().split()
N=int(s[0])
M=int(s[1])
adj=[[-1 for i in range(N)] for j in range(N)]
for i in range(N):
    adj[i][i]=0
for m in xrange(M):
    s=raw_input().split()
    x=int(s[0])
    y=int(s[1])
    r=int(s[2])
    adj[x-1][y-1]=r
    adj[y-1][x-1]=r
start=int(raw_input())
V=[]
mst=[start]
for i in xrange(1,N+1):
    V.append(i)
V.remove(start)
prim(mst,V,adj)
