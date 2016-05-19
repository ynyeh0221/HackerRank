# Enter your code here. Read input from STDIN. Print output to STDOUT

edgelength=6

def BFS(A,Q,start):
    while len(Q)>0:
        current=Q.pop(0)
        for i in xrange(len(A)):
            if visited[i]==False and A[current][i]==1:
                distance[i]=distance[current]+edgelength
                Q.append(i)
                visited[i]=True
    distance.pop(start-1)
    for i in xrange(len(distance)):
        if distance[i]==0:
            distance[i]=-1
    print " ".join(str(e) for e in distance)

T=int(raw_input())
for testcase in xrange(T):
    s=raw_input().split()
    N=int(s[0])
    M=int(s[1])
    adj=[[0 for i in range(N)] for j in range(N)]
    visited=[False for i in range(N)]
    distance=[0 for i in range(N)]
    queue=[]
    for m in xrange(M):
        s=raw_input().split()
        x=int(s[0])
        y=int(s[1])
        adj[x-1][y-1]=1
        adj[y-1][x-1]=1
    start=int(raw_input())
    visited[start-1]=True
    queue.append(start-1)
    BFS(adj,queue,start)
