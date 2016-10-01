D = int(raw_input())
for d in xrange(D):
    [S, P, Q] = raw_input().split()
    S = int(S)
    n = len(P)
    diff = [[0 for j in xrange(1500)] for i in xrange(1500)]
    for i in xrange(n):
        for j in xrange(n):
            if P[i] != Q[j]:
                diff[i][j] = 1
    res = -1
    for i in xrange(n):
        sum_before_start1 = sum_before_start2 = sum_before_end1 = sum_before_end2 = 0
        start1 = start2 = -1
        for end in xrange(0, n-i):
            sum_before_end1 += diff[end][i+end]
            sum_before_end2 += diff[i+end][end]
            while i+start1 < 1499 and sum_before_end1 - sum_before_start1 > S:
                start1 += 1
                sum_before_start1 += diff[start1][i+start1]
            while i+start2 < 1499 and sum_before_end2 - sum_before_start2 > S:
                start2 += 1
                sum_before_start2 += diff[i+start2][start2]

            if end - start1 > res:
                res = end - start1
            if end - start2 > res:
                res = end - start2
    print res
