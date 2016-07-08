# timeout

# Enter your code here. Read input from STDIN. Print output to STDOUT
def cal_V(path):
    v = 0
    for i in xrange(1,N+1):
        temp = i
        for j in xrange(1, i):
            if path[j-1] >= path[i-1]:
                temp = i-j
        v += temp
    return v

def DFS(path, visited, res):
    if len(path) == N:
        res += [cal_V(path)]
        return
    for i in xrange(N):
        if not visited[i]:
            if i>0 and not visited[i-1] and Y[i] == Y[i-1]:
                continue
            visited[i] = True
            DFS(path + [Y[i]], visited, res)
            visited[i] = False

T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    Y = map(int, raw_input().split(' '))
    res = []
    visited = [False for i in xrange(N)]
    DFS([], visited, res)
    temp = sum(res)/float(len(res))
    print "%.2f" % temp
