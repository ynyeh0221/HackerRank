def BFS(adj,start):
    while len(Q)>0:
        current=Q.pop(0)-1
        for i in xrange(1,N+1):
            if visit[i-1]==False and adj[current][i-1]==1:
                level[i-1]=level[current]+1
                Q.append(i)
                visit[i-1]=True

root=1
s=raw_input().split()
N=int(s[0])
M=int(s[1])
adj=[[0 for i in range(N)] for j in range(N)]
level=[0 for i in range(N)]
num_of_child=[1 for i in range(N)]
visit=[False for i in range(N)]
Q=[root]
for m in xrange(M):
    s=raw_input().split()
    x=int(s[0])
    y=int(s[1])
    #adj[x-1][y-1]=1
    adj[y-1][x-1]=1
if visit[root-1]==False:
    visit[root-1]=True
    BFS(adj,root)

maxx=max(level)
j=1
while j<=maxx:
    for i in xrange(1,N+1):
        if level[i-1]==maxx-j:
            for k in xrange(1,N+1):
                if adj[i-1][k-1]==1:
                    num_of_child[i-1]+=num_of_child[k-1]
    j+=1

result=-1
for i in num_of_child:
    if i%2==0:
        result+=1
print result
