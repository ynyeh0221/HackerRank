# wrong for 14, 18, 23

import heapq

[N,K] = map(int, raw_input().split())
A = map(int, raw_input().split())
heapq.heapify(A)
res = 0
if sum(A) >= K:
    while A[0] < K and res <= N:
        res += 1
        temp1 = heapq.heappop(A)
        temp2 = heapq.heappop(A)
        heapq.heappush(A, temp1 + 2 * temp2)
    print res if res <= N else -1
else:
    print -1
