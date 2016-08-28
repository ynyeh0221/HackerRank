q = int(raw_input())
for qq in xrange(q):
    n = int(raw_input())
    matrix = []
    for i in xrange(2 * n):
        matrix += [map(int, raw_input().split(' '))]
    m1 = []
    m2 = []
    m3 = []
    m4 = []
    for i in xrange(n):
        m1 += [matrix[i][:n]]
        m2 += [matrix[i][n:][::-1]]
    for i in xrange(n, 2*n):
        m3 += [matrix[i][:n]]
        m4 += [matrix[i][n:][::-1]]
    m3 = m3[::-1]
    m4 = m4[::-1]
    res = 0
    #res = [[0 for j in xrange(n)] for i in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            #res[i][j] = max(m1[i][j], m2[i][j], m3[i][j], m4[i][j])
            res += max(m1[i][j], m2[i][j], m3[i][j], m4[i][j])
    print res
