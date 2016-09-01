import sys

[N, M] = map(int, raw_input().split(' '))
edges = {}
weight_of_mst = 0
for i in xrange(1, N+1):
    edges[i] = []
for m in xrange(M):
    [x, y, r] = map(int, raw_input().split(' '))
    edges[x] += [[y,r]]
    edges[y] += [[x,r]]
start = int(raw_input())
in_mst = set([start])
while len(in_mst) < N:
    minn = sys.maxint
    minnode = -1
    for i in in_mst:
        for j in edges[i]:
            if j[0] not in in_mst:
                if j[1] < minn:
                    minn = j[1]
                    minnode = j[0]
    if minnode > 0:
        in_mst.add(minnode)
        weight_of_mst += minn
print weight_of_mst
