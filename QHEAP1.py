#testcase 8, 9 timeout

import heapq
T = int(raw_input())
h = []
for t in xrange(T):
    s = map(int, raw_input().split())
    if s[0] == 1:
        heapq.heappush(h, s[1])
    elif s[0] == 2:
        i = h.index(s[1])
        h[i] = h[-1]
        h.pop()
        heapq.heapify(h)
    else:
        print h[0]
